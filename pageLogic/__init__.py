from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "cartData.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "Powerkids!23"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    from .models import CartItem

    with app.app_context(): 
        db.create_all()
        print("Created Database")
    
    return app