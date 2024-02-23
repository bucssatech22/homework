from flask import Flask, redirect, url_for, render_template, session, request

app = Flask(__name__)
app.secret_key = "sgdgfdsggrg"

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'shopping_cart' not in session:
        session['shopping_cart'] = []

    if request.method == 'POST' and request.form.get('item'):
        item = request.form['item']
        session['shopping_cart'].append(item)
        session.modified = True

    return render_template('home.html', shopping_cart=session['shopping_cart'])

@app.route('/remove_item', methods=['POST'])
def remove_item():
    if 'shopping_cart' in session and request.method == 'POST':
        item_to_remove = request.form.get('item_to_remove')
        if item_to_remove in session['shopping_cart']:
            session['shopping_cart'].remove(item_to_remove)
            session.modified = True
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()

