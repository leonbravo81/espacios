# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/home")
def hello():
    return "Hello, World!"

@app.route("/login")
def login():
    return "Actualmente esta logueado"