from flask import Flask, render_template, request, redirect, session, url_for
from pageLogic import input_item_logic

app = Flask(__name__)

app.secret_key = "snjdnndskjnSkdlbawljicbasdkj"

@app.route('/', methods = ['GET', 'POST'])
def input_item():
    return input_item_logic.input_item()

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 5000)