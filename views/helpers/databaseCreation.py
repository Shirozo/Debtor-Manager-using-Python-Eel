def db_creation():
    """
    Initializing database table
    """
    from cs50 import SQL
    from werkzeug.security import generate_password_hash

    open("./views/database/database.db", "w")
    db = SQL("sqlite:///views/database/database.db")
    db.execute("""CREATE TABLE IF NOT EXISTS exdafgf ( 
                hyansasd
                )""")
    db.execute("INSERT INTO exdafgf (hyansasd) VALUES (?)", generate_password_hash(password="admin"))
    db.execute("""CREATE TABLE IF NOT EXISTS debt(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                name TEXT NOT NULL, 
                loan REAL NOT NULL, 
                balance REAL,
                due_date TEXT NOT NULL, 
                status TEXT NOT NULL)
            """)
    db.execute(""" CREATE TABLE IF NOT EXISTS d_transaction (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                userID INTEGER NOT NULL, 
                paymentAMOUNT REAL NOT NULL,
                transacType TEXT NOT NULL, 
                datePAID TEXT NOT NULL)
                """)
    db.execute("CREATE INDEX IF NOT EXISTS borrower ON debt (id)")
    db.execute("CREATE INDEX IF NOT EXISTS transactions ON d_transaction (userID)")