from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'qwertyuiop'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/shopping', methods = ['GET','POST'])

def shopping():
    if not session['shopping_list']:
        session['shopping_list'] = []

    if request.method == 'POST': 
        if 'add' in request.form: #button name -> a form
            item_added = request.form['new_item']  #找到new_item 在 dictionary 的value
            session_new = session['shopping_list']
            session_new.append(item_added)
            session['shopping_list'] = session_new

        elif 'delete' in request.form:
            item_removed = request.form['delete_item']
            session_new = session['shopping_list']
            session_new.remove(item_removed)
            session['shopping_list'] = session_new
            

        return redirect(url_for('shopping')) #每次执行完一次操作需要刷新一次界面, make a new GET request
    
    #Make the contents of session['shopping_list'] available to the template under the variable name shopping_list
    return render_template('shopping.html') 



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
