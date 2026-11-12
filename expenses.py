from validation import check_date, check_amount, check_text


def get_expense_details():
    date = input("Enter date (MM-DD-YYYY): ")
    check_date(date)
    description = check_text(input("Enter description: "))
    amount = check_amount(input("Enter amount: "))
    return {"date": date, "description": description, "amount": amount}
