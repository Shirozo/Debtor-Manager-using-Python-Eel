def check_due():
    """
    Check if Someone is past their due date
    """

    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    from cs50 import SQL
    while True:
        try:
            db = SQL("sqlite:///views/database/database.db")
            break
        except Exception:
            import views.helpers.databaseCreation as create
            create.db_creation()

    get_day = datetime.now()
    today = (get_day.strftime("%Y-%m-%d")).split("-")
    users = db.execute("SELECT * FROM debt WHERE status = 1")
    for user in users:
        due_date = (user["due_date"]).split("-")
        if datetime(int(today[0]), int(today[1]), int(today[2])) >= datetime(int(due_date[0]), int(due_date[1]), int(due_date[2])):
            tenPercent = user["balance"] * .10
            new_balance = user["balance"] + tenPercent
            plusMonth = datetime(int(due_date[0]), int(due_date[1]), int(due_date[2])) + relativedelta(months=1)
            new_due_date = plusMonth.strftime("%Y-%m-%d")
            db.execute("UPDATE debt SET balance = ?, due_date = ? WHERE id = ?", new_balance, new_due_date, user["id"])
            db.execute("INSERT INTO d_transaction(datePAID, paymentAMOUNT, userID, transacType) VALUES(?, ?, ?, ?)",user["due_date"], tenPercent, user["id"], "Due Date")