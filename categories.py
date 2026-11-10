from files import load_file, save_file
from validation import check_text


def show_categories(file_name):
    data = load_file(file_name)
    print("Current categories:")
    for category in data["categories"]:
        print(category)
    return data


def add_category(file_name):
    data = show_categories(file_name)
    name = check_text(input("Enter new category name: "))
    if name in data["categories"]:
        raise Exception("That category already exists.")
    data["categories"].append(name)
    save_file(file_name, data)
    print("Category added.")
