import mysql.connector
from pagelogic import login_logic, shopping_cart_logic
from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)

######## Login Page
@app.route('/login', methods=['GET', 'POST'])
# '/login': 
def login():
    return login_logic.login()

######## shopping cart page
@app.route('/shopping_cart', methods=['GET','POST'])
# '/shopping_cart':
def shopping_cart_logic():
    return shopping_cart_logic.shopping_cart()