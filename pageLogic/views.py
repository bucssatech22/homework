from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from . import db
from .models import CartItem

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        if 'delete_items' in request.form:
            selected_items = request.form.getlist('selected_items')
            print("selected_items: ", selected_items)
            items_to_delete = CartItem.query.filter(CartItem.name.in_(selected_items)).all()
            print("items_to_delete: ", items_to_delete)
            for item in items_to_delete:
                db.session.delete(item)
            db.session.commit()
        elif 'add_items' in request.form:
            itemName = request.form.get('new_item')
            #print("itemName: ", itemName)
            new_item = CartItem(name=itemName)
            #print("new_item.name: ", new_item.name)
            db.session.add(new_item)
            db.session.commit()
        
        return redirect(url_for('views.home'))

    itemList = CartItem.query.all()

    return render_template("home.html", itemList=itemList)
    
    
    
    