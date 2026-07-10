
import expense

with open("expenses.txt", "a") as file:
    print("\nYour Current Expenses:")
    print(expense.list())

while True:
    print("\n1. Add Expense")
    print("2. Remove Expense")
    print("3. List of Expenses")
    print("4. Calculate Total Expenses")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    if choice == '1':
        description = input("\nEnter Expense: ").title().strip()
        amount = float(input("Enter Amount: "))
        print(expense.add(description, amount))
    elif choice == '2':
        print(expense.list())
        description = input("\nWhich Expense do you wish to remove: ").title().strip()
        print(expense.remove(description))
    elif choice == '3':
        items = expense.list()
        if (items == ""):
            print("No expenses yet.")
        else:
            print("\nExpenses:")
            for item in items:
                print(f"{item}")
    elif choice == '4':
        print(f"Total Expenses: ${expense.calculate():.2f}")
    elif choice == '5':
        print("\nGoodbye!\n")
        break
    else:
        print("Invalid option, try again.\n")