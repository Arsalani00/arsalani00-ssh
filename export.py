import os
from files import load_file


def csv_text(value):
    result = '"'
    for character in value:
        if character == '"':
            result += '"'
        result += character
    return result + '"'


def export_csv(file_name, csv_name):
    data = load_file(file_name)
    if os.path.exists(csv_name):
        raise Exception("That file already exists. Choose another name.")
    with open(csv_name, "w", encoding="utf-8") as file:
        file.write("Date,Category,Description,Amount\n")
        for expense in data["expenses"]:
            date = csv_text(expense["date"])
            category = csv_text(expense["category"])
            description = csv_text(expense["description"])
            amount = f"{expense['amount']:.2f}"
            file.write(date + "," + category + "," + description + "," + amount + "\n")
    print("CSV file exported.")
