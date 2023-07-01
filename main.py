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
import json

db = SQL("sqlite:///views/database/database.db")

eel.init("views")

@eel.expose
def login(password : str) -> object: 
    """
    Return `true` if the password matches the hash password in the database.
    Otherwise, return `false`.
    """
    
    hash_pass = db.execute("SELECT hyansasd FROM exdafgf")[0]
    if check_password_hash(hash_pass["hyansasd"], password):
        return json.dumps({"code":200})
    else:
        return json.dumps({"code":405})


@eel.expose
def change_pass(new_password : str) -> None:
    """
    Eel function that `change the password` in the database.
    """

    new_pass_hash = generate_password_hash(new_password)
    db.execute("UPDATE exdafgf SET hyansasd = ?", new_pass_hash)


@eel.expose
def fetch_data(order : str, select : str = "%" ) -> object:
    """
    This function `fetches` all the `data` in the database based on
    their `order` and what data to `select`. If the fetch data is empty, it 
    would just return an `empty list`.
    """

    if order.lower() == "balance":
        datas = db.execute("SELECT * FROM debt WHERE name LIKE ? ORDER BY balance DESC LIMIT 15", select)
    elif order.lower() == "due date":
        datas = db.execute("SELECT * FROM debt WHERE name LIKE ? ORDER BY due_date LIMIT 15", select)
    else:
        datas = db.execute("SELECT * FROM debt WHERE name LIKE ? ORDER BY name LIMIT 15", select)
    return json.dumps(datas)


@eel.expose
def add_debt(name : str, amount : float, dueDate : str) -> None:
    """
    `Add` new debt or borrower to the database.
    """

    db.execute("INSERT INTO debt(name, loan, balance, due_date) VALUES(?, ?, ?, ?)", name.title(), amount, amount, dueDate)
    return


@eel.expose
def date_checker(DateTime : str, due_d : str ="") -> bool:
    """
    The funtion validates the due date of the borrower.
    If the `due_d` variable if empty, the function would just validate
    if the `DateTime` or `due_date` of the borrower is greater than the date today.
    Return `true` if the DateTime is valid. Otherwise, return `false`.\n
    If the the `due_d` argument is not empty, meaning validating if the 
    `DateTime` didn't pass the `due_d or due date`. Then it would return `true`
    and `false` otherwise.
    """

    dateTime = DateTime.split("-")
    if not due_d:
        if datetime(int(dateTime[0]), int(dateTime[1]), int(dateTime[2])) > datetime.now():
            return True
        return False
    else:
        due_date = due_d.split("-")
        if datetime(int(dateTime[0]), int(dateTime[1]), int(dateTime[2])) <= datetime(int(due_date[0]), int(due_date[1]), int(due_date[2])):
            return True
        return False


@eel.expose
def remover(idRM : int) -> None:
    """
    A function to remove a data of the borrower from the database.
    """

    db.execute("PRAGMA foreign_keys = ON")
    db.execute("DELETE FROM debt WHERE id = ?", idRM)
    db.execute("PRAGMA foreign_keys = OFF")
    return


@eel.expose
def fetch_single_user(user_id : int) -> object:
    """
    Function to fetch a single user in the database.
    """
    user_data = db.execute("SELECT * FROM debt WHERE id = ?", user_id)
    return json.dumps(user_data)

@eel.expose
def debtpay(id, amount, datepaid):
    return None
eel.start("templates/login.html",
            disable_cache = True)