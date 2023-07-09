def add_borrower(name : str, amount : float, dueDate : str) -> None:
    """
    `Add` new debt or borrower to the database.
    """
    from cs50 import SQL
    db = SQL("sqlite:///views/database/database.db")

    db.execute("INSERT INTO debt(name, loan, balance, due_date, status) VALUES(?, ?, ?, ?, True)", name.title(), amount, amount, dueDate)
    return