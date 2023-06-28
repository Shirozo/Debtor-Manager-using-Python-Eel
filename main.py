import sys
from io import StringIO
if sys.stdout is None:
    sys.stdout = StringIO()
if sys.stderr is None:
    sys.stderr = StringIO()
import eel
import flask
from cs50 import SQL
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQL("sqlite:///views/database/database.db")

eel.init("views")

@eel.expose
def login(password):
    hash_pass = db.execute("SELECT hyansasd FROM exdafgf")[0]
    if check_password_hash(hash_pass["hyansasd"], password):
        return True
    else:
        return False
    
@eel.expose
def change_pass(new_password):
    new_pass_hash = generate_password_hash(new_password)
    db.execute("UPDATE exdafgf SET hyansasd = ?", new_pass_hash)

@eel.expose
def fetch_data(order):
    if order.lower() == "balance":
        datas = db.execute("SELECT * FROM debt ORDER BY balance DESC")
    elif order.lower() == "due date":
        datas = db.execute("SELECT * FROM debt ORDER BY due_date")
    else:
        datas = db.execute("SELECT * FROM debt ORDER BY name")
    return datas


@eel.expose
def add_debt(name, amount, dueDate):
    db.execute("INSERT INTO debt(name, loan, balance, due_date) VALUES(?, ?, ?, ?)", name.title(), amount, amount, dueDate)
    return

@eel.expose
def date_checker(DateTime):
    dateTime = DateTime.split("-")
    if datetime(int(dateTime[0]), int(dateTime[1]), int(dateTime[2])) > datetime.now():
        return True
    return False

@eel.expose
def remover(idRM):
    db.execute("PRAGMA foreign_keys = ON")
    db.execute("DELETE FROM debt WHERE id = ?", idRM)
    db.execute("PRAGMA foreign_keys = OFF")
    return

eel.start("templates/login.html",
            disable_cache = True)