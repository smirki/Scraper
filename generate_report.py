```
def generate_report(start_date: str, end_date: str) -> str:
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    time delta = end_date_obj - start_date_obj
    
    days = time delta.days
    months = days // 30
    years = days // 365
    
    if years > 0:
        if years == 1:
            years_str = 'year'
        else:
            years_str = 'years'
        report = f"The report covers a period of {years} {years_str}."
    elif months > 0:
        if months == 1:
            months_str = 'month'
        else:
            months_str = 'months'
        report = f"The report covers a period of {months} {months_str}."
    else:
        report = f"The report covers a period of {days} days."
    
    return report
```