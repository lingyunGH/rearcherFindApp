from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/single')
@app.route('/single.html')
def single():
    return render_template("single.html")

@app.route('/register')
@app.route('/register.html')
def register():
    return render_template("register.html")