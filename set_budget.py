def set_budget(amount: float, category: str) -> None:
    budget = {}
    if category in budget:
        budget[category] = amount
    else:
        print("Category not recognized. Please check your budget categories.")