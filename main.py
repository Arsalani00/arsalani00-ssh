from files import create_file
from expenses import add_expense


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
        elif choice == "5":
            file_name = input("Enter expense file name: ")
            add_expense(file_name)


if __name__ == "__main__":
    main()
