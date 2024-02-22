from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from os import path

# db = SQLAlchemy()
# DB_NAME = "database.db"



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app
