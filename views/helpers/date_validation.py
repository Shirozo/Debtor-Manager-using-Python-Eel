def datevldt(DateTime : str, due_d: str) -> bool:
    """
    The funtion validates the due date of the borrower.
    If the `due_d` variable if empty, the function would just validate
    if the `DateTime` or `due_date` of the borrower is greater than the date today.
    Return `true` if the DateTime is valid. Otherwise, return `false`.\n
    If the the `due_d` argument is not empty, meaning validating if the 
    `DateTime` didn't pass the `due_d or due date`. Then it would return `true`
    and `false` otherwise.
    """
    
    from datetime import datetime

    dateTime = DateTime.split("-")
    if not due_d:
        if datetime(int(dateTime[0]), int(dateTime[1]), int(dateTime[2])) > datetime.now():
            return True
        return False
    else:
        due_date = due_d.split("-")
        if datetime(int(dateTime[0]), int(dateTime[1]), int(dateTime[2])) <= datetime(int(due_date[0]), int(due_date[1]), int(due_date[2])):
            return True
        return False