from flask import Flask, redirect, url_for, render_template, session, request

app = Flask(__name__)

app.secret_key = "sgdgfdsggrg"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)