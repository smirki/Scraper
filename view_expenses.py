```
def view_expenses(start_date, end_date):
    expenses = [
        {"date": "2022-01-10", "amount": 100.0},
        {"date": "2022-01-12", "amount": 50.0},
        {"date": "2022-02-14", "amount": 200.0},
        {"date": "2022-02-20", "amount": 300.0},
        {"date": "2022-03-10", "amount": 400.0}
    ]

    filtered_expenses = [expense for expense in expenses if start_date <= expense["date"] <= end_date]
    
    return filtered_expenses