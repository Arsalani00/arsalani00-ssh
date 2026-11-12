from files import create_file, load_file
from expenses import add_expense, show_expenses, filter_expenses
from export import export_csv


def main():
    choice = ""
    while choice != "6":
        print("\n1. Create Expense File")
        print("2. Load Expense File")
        print("3. Export Expense File to CSV")
        print("4. Edit Expense Categories")
        print("5. Add Expenses")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            file_name = input("Enter expense file name: ")
            create_file(file_name)
        elif choice == "2":
            file_name = input("Enter expense file name: ")
            data = load_file(file_name)
            category = input("Category (blank for all): ")
            start_date = input("Start date MM-DD-YYYY (blank for no limit): ")
            end_date = input("End date MM-DD-YYYY (blank for no limit): ")
            filtered = filter_expenses(data["expenses"], category, start_date, end_date)
            show_expenses(filtered)
        elif choice == "3":
            file_name = input("Enter expense file name: ")
            csv_name = input("Enter CSV file name (example: expenses.csv): ")
            export_csv(file_name, csv_name)
        elif choice == "5":
            file_name = input("Enter expense file name: ")
            add_expense(file_name)


if __name__ == "__main__":
    main()
