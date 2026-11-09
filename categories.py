from files import load_file


def show_categories(file_name):
    data = load_file(file_name)
    print("Current categories:")
    for category in data["categories"]:
        print(category)
    return data
