import json
import os


def save_file(file_name, data):
    json_text = json.dumps(data)
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(json_text)


def create_file(file_name):
    if file_name == "":
        raise Exception("Enter a file name.")
    if os.path.exists(file_name):
        raise Exception("That file already exists. Choose Load Expense File.")
    data = {"categories": ["Food", "Transportation", "Other"], "expenses": []}
    save_file(file_name, data)
    print("Expense file created.")
