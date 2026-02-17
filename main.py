from expense import add_expense, get_all_expenses
from my_validators import validate_amount, validate_category, validate_date


def show_menu():
    print("\nTallyRoom")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Amount: "))
                validate_amount(amount)

                category = input("Category: ")
                validate_category(category)

                date = input("Date (dd/mm/yyyy): ")
                validate_date(date)

                note = input("Note: ")

                add_expense(amount, category, date, note)
                print("Expense added successfully!")

            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            expenses = get_all_expenses()

            if not expenses:
                print("No expenses found.")
            else:
                for expense in expenses:
                    print("\nID:", expense[0])
                    print("Amount:", expense[1])
                    print("Category:", expense[2])
                    print("Date:", expense[3])
                    print("Note:", expense[4])
                    print("----------------------")

        elif choice == "3":
          print("Exiting TallyRoom. Goodbye!")
          break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
