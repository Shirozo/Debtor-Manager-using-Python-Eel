from flask import Flask, render_template, redirect, flash, request, session, jsonify
from cs50 import SQL
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required
from os import mkdir


app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies) C: CS50
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#Configure a database
try:
    s = open('./database/database.db')
except (FileExistsError, FileNotFoundError):
    mkdir("database")
    s = open('./database/database.db', 'w')
    db = SQL("sqlite:///database/database.db")
    db.execute("CREATE TABLE IF NOT EXISTS exdafgf ( hyansasd )")
    db.execute("CREATE TABLE IF NOT EXISTS debtor (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL)")
    db.execute("INSERT INTO exdafgf (hyansasd) VALUES (?)", generate_password_hash("admin"))

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
    try:
        session["user"]
        return render_template("index.html")
    except KeyError:
        return redirect("/login")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        pwd = request.form.get("password").strip()
        hash_pass = db.execute("SELECT hyansasd FROM exdafgf")[0]
        print(pwd)
        if check_password_hash(hash_pass["hyansasd"], pwd):
            user_hash = generate_password_hash("user")
            session['user'] = user_hash
            return redirect("/")
        else:
            flash("Incorrect Password")
            return redirect("/login")
    else:
        return render_template("login.html")
    

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")