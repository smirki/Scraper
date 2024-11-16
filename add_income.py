def add_income(source, amount):
    income_list = {
        'monthly': {'housing': 0, 'food': 0, 'entertainment': 0, 'savings': 0},
        'yearly': {'housing': 0, 'food': 0, 'entertainment': 0, 'savings': 0},
        'one-time': {'housing': 0, 'food': 0, 'entertainment': 0, 'savings': 0}
    }
    income_list[source][source.capitalize()] += amount
    return income_list