from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)

app.secret_key = 'secret_key'

@app.route('/')
def index():
    cart_items = session.get('cart_items', [])
    return render_template('shopping_cart.html', cart_items=cart_items)


@app.route('/add', methods=['POST'])
def add_to_cart():
    item = request.form.get('verif')
    if 'cart_items' not in session:
        session['cart_items'] = []
    session['cart_items'].append(item)
    session.modified = True
    return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove_from_cart():
    item_to_remove = request.form.get('verif_remove')  
    if 'cart_items' in session:
        if item_to_remove in session['cart_items']:  
            session['cart_items'].remove(item_to_remove) 
            session.modified = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
