import eel
from os import mkdir
from cs50 import SQL
from werkzeug.security import generate_password_hash, check_password_hash
import json

db = SQL("sqlite:///views/database/database.db")


eel.init("views")

@eel.expose
def login(password):
    hash_pass = db.execute("SELECT hyansasd FROM exdafgf")[0]
    if check_password_hash(hash_pass["hyansasd"], password):
        return True
    else:
        return False

eel.start("templates/login.html")