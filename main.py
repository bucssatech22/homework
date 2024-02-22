from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)

app.secret_key = 'secret_key'

@app.route('/')

def index():
    return render_template('shoppingcart.html')

@app.route('/add', methods=['POST'])

def add_to_cart():
    item = request.form.get('verif')
    if 'cart_items' not in session:
        session['cart_items'] = []
    session['cart_items'].append(item)
    session.modified = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)