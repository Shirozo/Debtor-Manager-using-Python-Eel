from flask import redirect, session
from functools import wraps

def login_required(f):
    """
    Decorate to require login.
    
    https://flask.palletsproject.com/en/1.1.x/patterns/viewdecorators
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            return redirect("/log_in")
        return f(*args, **kwargs)
    return decorated_function