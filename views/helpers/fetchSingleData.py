def singleUser(user_id : int) -> list[dict]:
    """
    Function to fetch a single user in the database.
    """
    from cs50 import SQL

    db = SQL("sqlite:///views/database/database.db")

    user_data = db.execute("SELECT * FROM debt WHERE id = ?", user_id)
    return user_data