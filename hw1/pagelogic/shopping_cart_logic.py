from flask import Flask, render_template, request, redirect, session, url_for, flash
import mysql.connector
import config

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 设置 Flask session 密钥

@app.route('/shopping_cart', methods=['GET', 'POST'])
def shopping_cart():
    if request.method == 'POST':
        email = request.form['email']
        item_id = request.form['item_id']
        action = request.form['action']  # 假设是 'add' 或 'remove'

        mydb = config.mydb()
        cur = mydb.cursor(buffered=True, dictionary=True)

        # 检查商品是否存在
        cur.execute('SELECT * FROM cart_items WHERE email = %s AND item_id = %s', (email, item_id))
        item = cur.fetchone()

        if item:
            # 商品存在，根据操作更新数量
            if action == 'add':
                new_quantity = item['quantity'] + 1
                cur.execute('UPDATE cart_items SET quantity = %s WHERE email = %s AND item_id = %s', (new_quantity, email, item_id))
            elif action == 'remove':
                # 如果数量大于1，则减少数量，否则从购物车中删除商品
                if item['quantity'] > 1:
                    new_quantity = item['quantity'] - 1
                    cur.execute('UPDATE cart_items SET quantity = %s WHERE email = %s AND item_id = %s', (new_quantity, email, item_id))
                else:
                    cur.execute('DELETE FROM cart_items WHERE email = %s AND item_id = %s', (email, item_id))
            mydb.commit()
        else:
            # 商品不存在
            flash('商品不存', 'error')
            return render_template('error_page.html')  # 假设有一个错误页面模板

        return redirect(url_for('shopping_cart'))
    else:
        # GET 请求逻辑，显示购物车页面
        return render_template('shopping_cart.html')

if __name__ == '__main__':
    app.run(debug=True)
