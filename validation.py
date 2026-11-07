from datetime import datetime


def check_date(value):
    parts = value.split("-")
    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])
    return datetime(year, month, day)
