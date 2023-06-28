import sys
from io import StringIO
if sys.stdout is None:
    sys.stdout = StringIO()
if sys.stderr is None:
    sys.stderr = StringIO()
import eel
from cs50 import SQL
from werkzeug.security import generate_password_hash, check_password_hash

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
def fetch_data():
    datas = db.execute("SELECT * FROM debt ORDER BY name")
    return datas

eel.start("templates/login.html",
            disable_caache = True)