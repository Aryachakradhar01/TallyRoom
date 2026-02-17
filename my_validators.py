def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")


def validate_category(category):
    if not category.strip():
        raise ValueError("Category cannot be empty")


from datetime import datetime

def validate_date(date):
    try:
        datetime.strptime(date, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Date must be DD/MM/YYYY")
