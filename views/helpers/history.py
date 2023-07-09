def hist(uid : int) -> list[dict]:
    """Return all the transaction history of the user"""
    from cs50 import SQL
    db = SQL("sqlite:///views/database/database.db")

    history = db.execute("SELECT * FROM d_transaction WHERE userID = ? ORDER BY datePAID", uid)
    return history