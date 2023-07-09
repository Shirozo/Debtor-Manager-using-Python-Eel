def fetchData(order : str, qstatus : int ,select : str = "%") -> dict:
    """
    This function `fetches` all the `data` in the database based on
    their `order` and what data to `select`. If the fetch data is empty, it 
    would just return an `empty list`.
    """
    from cs50 import SQL

    db = SQL("sqlite:///views/database/database.db")

    if order.lower() == "balance":
        datas = db.execute("SELECT * FROM debt WHERE name LIKE ? AND STATUS = ? ORDER BY balance DESC", select, qstatus)
    elif order.lower() == "due date":
        datas = db.execute("SELECT * FROM debt WHERE name LIKE ? AND STATUS = ? ORDER BY due_date", select, qstatus)
    else:
        datas = db.execute("SELECT * FROM debt WHERE name LIKE ? AND STATUS = ? ORDER BY name", select, qstatus) 
    return datas