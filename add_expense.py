```
def add_expense(category, amount):
    expense_list = {"Food": 0.0, "Transportation": 0.0, "Entertainment": 0.0}
    if category in expense_list:
        expense_list[category] += amount
    else:
        print("Invalid category. Please choose from Food, Transportation, or Entertainment.")
    return expense_list