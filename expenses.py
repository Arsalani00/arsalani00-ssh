from validation import check_date, check_amount, check_text
from categories import show_categories
from files import save_file


def get_expense_details():
    date = input("Enter date (MM-DD-YYYY): ")
    check_date(date)
    description = check_text(input("Enter description: "))
    amount = check_amount(input("Enter amount: "))
    return {"date": date, "description": description, "amount": amount}


def add_expense(file_name):
    data = show_categories(file_name)
    category = check_text(input("Enter category: "))
    if category not in data["categories"]:
        raise Exception("Choose a category from the list.")
    expense = get_expense_details()
    expense["category"] = category
    data["expenses"].append(expense)
    save_file(file_name, data)
    print("Expense added.")


def show_expenses(expenses):
    for expense in expenses:
        print("Date:", expense["date"])
        print("Category:", expense["category"])
        print("Description:", expense["description"])
        print(f"Amount: {expense['amount']:.2f}")
        print()


def filter_expenses(expenses, category):
    filtered = []
    for expense in expenses:
        if category == "" or expense["category"] == category:
            filtered.append(expense)
    return filtered
