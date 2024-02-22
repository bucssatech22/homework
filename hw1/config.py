from flask_mail import Mail
import mysql.connector

MAIL_SERVER = 'email-smtp.us-east-1.amazonaws.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = ''
MAIL_PASSWORD = ''


AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

mail = Mail()
def init_mail(app):
    mail.init_app(app)


def mydb():
    return mysql.connector.connect(
        host = "shopping_cart.us-east-1.rds.amazonaws.com",
        user = "admin",
        password = "shopping_cart_test",
        database = "shopping_cart_test_1"
    )
