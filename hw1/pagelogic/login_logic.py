from flask import render_template, request, redirect, session, url_for, flash
from utils import generate_session_token, password_utils, scheduler
import config


def login():
    if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            
            mydb = config.mydb()

            cur = mydb.cursor(buffered=True, dictionary=True)
            
            cur.execute('SELECT * FROM users WHERE email = (%s)', (email,))
            user = cur.fetchone()
            verified = False

            if user: #先看user是否存在，如果存在则验证password
                stored_password = bytes(user['password'])
                stored_salt = bytes(user['salt'])
                verified = password_utils.verify_password(password, stored_salt, stored_password)
            else:
                flash('用户不存在', category='error')
                return redirect(url_for('login'))

            if verified: #验证password成功后再进行常规加载
                cur.execute("SELECT verif_code FROM session_storage WHERE email = %s", (email,))
                stored_token = cur.fetchone()
                if stored_token:
                    cur.execute('DELETE FROM session_storage WHERE email = %s', (email, ))
                    mydb.commit()
                
                token = generate_session_token.generate_session_token()
                session['type'] = user['type']
                session['name'] = user['name']
                session['email'] = user['email']
                session['session_token'] = token
                
                cur.execute('INSERT INTO session_storage(email, verif_code) VALUES (%s, %s)', (email, token))
                mydb.commit()


            else:
                flash('密码不正确', category='error')
                return redirect(url_for('login'))
            

    return render_template("login.html")