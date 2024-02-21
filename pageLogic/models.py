from . import db

class CartItem(db.Model):
    __tablename__ = 'CartItem'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))