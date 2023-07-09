def In(pwd: str) -> int:
    """
    Return `true` if the password matches the hash password in the database.
    Otherwise, return `false`.
    """

    from werkzeug.security import check_password_hash
    from cs50 import SQL
    
    db = SQL("sqlite:///views/database/database.db")
    
    hash_pass = db.execute("SELECT hyansasd FROM exdafgf")[0]
    if check_password_hash(hash_pass["hyansasd"], password=pwd):
        return 200
    return 405