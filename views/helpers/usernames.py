def users() -> list:
    """
    Function to fetch just the `name` in the database.
    """
    from cs50 import SQL
    db = SQL("sqlite:///views/database/database.db")

    names = db.execute("SELECT id, name FROM debt ORDER BY status DESC, name")
    return names