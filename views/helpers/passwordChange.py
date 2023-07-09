def pwChange(new_password: str) -> int:
    """
    Eel function that `change the password` in the database.
    """
    
    from cs50 import SQL
    from werkzeug.security import generate_password_hash    
    
    db = SQL("sqlite:///views/database/database.db")

    new_pass_hash = generate_password_hash(password=new_password)
    db.execute("UPDATE exdafgf SET hyansasd = ?", new_pass_hash)

    return 200