def view_budget(category):
    budget_dict = {
        "housing": 1000.0,
        "food": 500.0,
        "transportation": 200.0,
        "entertainment": 100.0,
        "savings": 500.0
    }
    if category in budget_dict:
        return float(budget_dict[category])
    else:
        return -1.0