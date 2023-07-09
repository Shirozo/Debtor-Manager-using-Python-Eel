def rmf(idRM : int) -> None:
    """
    A function to remove a data of the borrower from the database.
    """
    from cs50 import SQL
    db = SQL("sqlite:///views/database/database.db")

    db.execute("PRAGMA foreign_keys = ON")
    db.execute("DELETE FROM debt WHERE id = ?", idRM)
    db.execute("PRAGMA foreign_keys = OFF")
    return