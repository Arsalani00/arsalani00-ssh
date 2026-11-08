from datetime import datetime


def check_date(value):
    parts = value.split("-")
    if len(parts) != 3:
        raise Exception("Use MM-DD-YYYY for dates.")
    if len(parts[0]) != 2 or len(parts[1]) != 2 or len(parts[2]) != 4:
        raise Exception("Use MM-DD-YYYY for dates.")
    for part in parts:
        for character in part:
            if character not in "0123456789":
                raise Exception("Use digits and hyphens for dates.")
    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])
    return datetime(year, month, day)


def check_amount(value):
    amount = float(value)
    if not (0 < amount <= 1000000000):
        raise Exception("Enter an amount greater than zero and at most 1000000000.")
    # Check whether displaying two decimals would change the amount.
    formatted_amount = f"{amount:.2f}"
    if amount != float(formatted_amount):
        raise Exception("Use at most two decimal places.")
    return amount
