from flask import Flask, render_template, redirect, flash, request, session, jsonify
from cs50 import SQL
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required


app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies) C: CS50
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#Configure a database
try:
    s = open('./database/database.db')
except (FileExistsError, FileNotFoundError):
    s = open('./database/database.db', 'w')
else:
    db = SQL("sqlite:///database/database.db")
    


@app.after_request
def after_request(response):
    """Ensure responses aren't cached C: CS50"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("layout.html") 