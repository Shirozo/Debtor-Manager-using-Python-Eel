from os.path import expanduser, join
from os import makedirs
import csv
from cs50 import SQL
from datetime import datetime
from dateutil.relativedelta import relativedelta

db = SQL("sqlite:///views/database/database.db")

def downloader(params = "all"):
    paths = expanduser('~/Downloads')
    folder = join(paths, "Datas")
    try:
        makedirs(folder)
    except Exception:
        pass
    if (params.lower() == "all"):
        datas = db.execute("SELECT * FROM debt")
        for data in datas:
            with open(f"{folder}/{data['name']}_{data['id']}.csv", "w", newline='') as userFILE:
                userFILE.write(f"Name: {data['name']}\n")
                userFILE.write(f"Loan Amount: {data['loan']}\n")
                userFILE.write(f"Balance: {data['balance']}\n")
                userFILE.write(f"Due Date: {data['due_date']}\n")
                userFILE.write(f"Status: {data['status']}\n\n")
                
                writer = csv.DictWriter(userFILE, fieldnames=["Amount", "","Date"])
                writer.writeheader()
                user_transaction = db.execute("SELECT * FROM d_transaction WHERE userID = ?", data["id"])
                for transac in user_transaction:
                    writer.writerow({"Amount" : f'{int(transac["paymentAMOUNT"])}', "Date" : transac["datePAID"].replace("-", "_"), "" : "\t"})

    else:
        single_user = db.execute("SELECT * FROM debt WHERE id = ?", params)[0]
        with open(f"{folder}/{single_user['name']}_{single_user['id']}.csv", "w", newline='',) as userFILE:
            userFILE.write(f"Name: {single_user['name']}\n")
            userFILE.write(f"Loan Amount: {single_user['loan']}\n")
            userFILE.write(f"Balance: {single_user['balance']}\n")
            userFILE.write(f"Due Date: {single_user['due_date']}\n")
            userFILE.write(f"Status: {single_user['status']}\n\n")

            writer = csv.DictWriter(userFILE, fieldnames=["Amount", "", "Date"])
            writer.writeheader()
            user_transaction = db.execute("SELECT * FROM d_transaction WHERE userID = ?", single_user["id"])
            for transac in user_transaction:
                writer.writerow({"Amount" : f'{int(transac["paymentAMOUNT"])}', "Date" : transac["datePAID"].replace("-", "_"), "" : "\t"})
    


def check_due():
    get_day = datetime.now()
    today = (get_day.strftime("%Y-%m-%d")).split("-")
    users = db.execute("SELECT * FROM debt WHERE status = 1")
    for user in users:
        due_date = (user["due_date"]).split("-")
        if datetime(int(today[0]), int(today[1]), int(today[2])) == datetime(int(due_date[0]), int(due_date[1]), int(due_date[2])):
            tenPercent = user["balance"] * .10
            new_balance = user["balance"] + tenPercent
            plusMonth = datetime(int(due_date[0]), int(due_date[1]), int(due_date[2])) + relativedelta(months=1)
            new_due_date = plusMonth.strftime("%Y-%m-%d")
            db.execute("UPDATE debt SET balance = ?, due_date = ? WHERE id = ?", new_balance, new_due_date, user["id"])
            db.execute("INSERT INTO d_transaction(datePAID, paymentAMOUNT, userID, transacType) VALUES(?, ?, ?, ?)", tenPercent, user["id"], user["due_date"])