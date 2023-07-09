import sys
from io import StringIO
if sys.stdout is None:
    sys.stdout = StringIO()
if sys.stderr is None:
    sys.stderr = StringIO()
import eel
import json
from pyautogui import size
import views.helpers.downloader as dl
import views.helpers.date_validation as valiDate
import views.helpers.login as loggIn
import views.helpers.passwordChange as pwdc
import views.helpers.fetchdata as dataFetch
import views.helpers.fetchSingleData as fetchSD
import views.helpers.usernames as users
import views.helpers.borrow as borrow
import views.helpers.remove as rm
import views.helpers.payment as payM
import views.helpers.history as History
import views.helpers.dueDate as due

#Imported for the sake of pyinstaller to compile properly. Don't Remove
import flask
from cs50 import SQL

eel.init('views')

@eel.expose
def login(password : str) -> object: 
    code = loggIn.In(pwd = password)
    return json.dumps({"code" : code})

@eel.expose
def change_pass(new_password : str) -> None:
    pwdc.pwChange(new_password=new_password)
    return

@eel.expose
def fetch_data(order : str, qstatus : int ,select : str = "%") -> object:
    datas = dataFetch.fetchData(order=order, qstatus=qstatus, select=select)
    return json.dumps(datas)

@eel.expose
def fetch_single_user(user_id : int) -> object:
    datas = fetchSD.singleUser(user_id=user_id)
    return json.dumps(datas)

@eel.expose
def fetch_username():
    name = users.users()
    return json.dumps(name)

@eel.expose
def add_debt(name : str, amount : float, dueDate : str) -> None:
    borrow.add_borrower(name=name, amount=amount, dueDate=dueDate)
    return

@eel.expose
def date_checker(DateTime : str, due_d : str =""):
    status = valiDate.datevldt(DateTime, due_d)
    return status

@eel.expose
def remover(idRM : int) -> None:
    rm.rmf(idRM=idRM)
    return

@eel.expose
def debtpay(uid : int, amount : float, datepaid : str, transactType : str = "Payment") -> object:
    status = payM.pay(uid=uid, amount=amount, datepaid=datepaid, transactType=transactType)
    return json.dumps({"status" : status})

@eel.expose
def download_data(uid):
    dl.downloader(uid)
    return

@eel.expose
def history(uid : int) -> object:
    data = History.hist(uid=uid)
    return json.dumps(data)

@eel.expose
def initializer():
    due.check_due()

eel.start("templates/login.html",
            disable_cache = True,
            size=(size()))