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
import helpers

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
def fetch_data(order : str, qstatus : int ,select : str = "%") -> object:
    """
    This function `fetches` all the `data` in the database based on
    their `order` and what data to `select`. If the fetch data is empty, it 
    would just return an `empty list`.
    """

    if order.lower() == "balance":
        datas = db.execute("SELECT * FROM debt WHERE name LIKE ? AND STATUS = ? ORDER BY balance DESC", select, qstatus)
    elif order.lower() == "due date":
        datas = db.execute("SELECT * FROM debt WHERE name LIKE ? AND STATUS = ? ORDER BY due_date", select, qstatus)
    else:
        datas = db.execute("SELECT * FROM debt WHERE name LIKE ? AND STATUS = ? ORDER BY name", select, qstatus) 
    return json.dumps(datas)


@eel.expose
def fetch_single_user(user_id : int) -> object:
    """
    Function to fetch a single user in the database.
    """
    user_data = db.execute("SELECT * FROM debt WHERE id = ?", user_id)
    return json.dumps(user_data)


@eel.expose
def fetch_username():
    """
    Function to fetch just the `name` in the database.
    """
    names = db.execute("SELECT id, name FROM debt ORDER BY status DESC, name")
    return json.dumps(names)


@eel.expose
def add_debt(name : str, amount : float, dueDate : str) -> None:
    """
    `Add` new debt or borrower to the database.
    """

    db.execute("INSERT INTO debt(name, loan, balance, due_date, status) VALUES(?, ?, ?, ?, True)", name.title(), amount, amount, dueDate)
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
def debtpay(uid : int, amount : float, datepaid : str, transactType : str = "Payment") -> object:
    """
    This function update your balance in the database. It takes an 3 argument:
    `id`, `amount`, and `datepaid`\n
    `id` is the id of the user or account.\n
    `amount` the amount paid for that date.\n
    `datepaid` when that debt was paid.\n
    This will then add the transaction to the database and update your balance.
    """
    try:
        balance = db.execute("SELECT balance FROM debt WHERE id = ?", uid)[0]["balance"]
        amount = float(amount)
        new_balance = balance - amount
        if new_balance <= 0:
            status = False
        else:
            status = True
        db.execute("INSERT INTO d_transaction(userID, paymentAMOUNT, datePAID, transacType) VALUES(?, ?, ?, ?)", uid, amount, datepaid, transactType)
        db.execute("UPDATE debt SET balance = ?, status = ? WHERE id = ?", new_balance, status, uid)
        return json.dumps({"status" : 200})
    except Exception as e:
        return json.dumps({"status" : 405})

@eel.expose
def download_data(uid):
    helpers.downloader(uid)
    return


@eel.expose
def history(uid : int) -> object:
    """Return all the transaction history of the user"""

    history = db.execute("SELECT * FROM d_transaction WHERE userID = ? ORDER BY datePAID", uid)
    return json.dumps(history)


@eel.expose
def initializer():
    """Check if anyone have already passed their due date"""
    helpers.check_due()

eel.start("templates/login.html",
            disable_cache = True)