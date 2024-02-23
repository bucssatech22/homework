from flask import Blueprint, Flask, render_template, request, redirect, session, url_for, flash
views = Blueprint('views', __name__)


# add sign in page, log in page, grocery page, add to list page, 





@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and 'add' in request.form:
        something = request.form['something']
        if 'cart_items' not in session:
            session['cart_items'] = []
        session['cart_items'].append(something)
        flash(f'{something} added to cart', category='success')
        return redirect(url_for('views.home'))

    return render_template("home.html")



@views.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST' and 'delete' in request.form:
        item_to_remove = request.form.get('deleteSomething')
        if item_to_remove in session.get('cart_items', []):
            session['cart_items'].remove(item_to_remove)
            flash(f'{item_to_remove} removed from cart', category='info')
            return redirect(url_for('views.cart'))


    cart_items = session.get('cart_items', [])
    return render_template("cart.html", cart_items=cart_items)



