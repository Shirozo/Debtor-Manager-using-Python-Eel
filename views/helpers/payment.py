def pay(uid : int, amount : float, datepaid : str, transactType : str = "Payment") -> int:
    """
    This function update your balance in the database. It takes an 3 argument:
    `id`, `amount`, and `datepaid`\n
    `id` is the id of the user or account.\n
    `amount` the amount paid for that date.\n
    `datepaid` when that debt was paid.\n
    This will then add the transaction to the database and update your balance.
    """
    from cs50 import SQL
    db = SQL("sqlite:///views/database/database.db")

    try:
        balance = db.execute("SELECT balance FROM debt WHERE id = ?", uid)[0]["balance"]
        amount = float(amount)
        new_balance = balance - amount
        if new_balance <= 0:
            status = False
        else:
            status = True
        db.execute("INSERT INTO d_transaction(userID, paymentAMOUNT, datePAID, transacType) VALUES(?, ?, ?, ?)", uid, amount, datepaid, transactType)
        db.execute("UPDATE debt SET balance = ?, status = ? WHERE id = ?", new_balance, status, uid)
        return 200 
    except Exception as e:
        return 405