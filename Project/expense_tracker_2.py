
expenses = []

def add_expense(description, amount):
    if amount <= 0:
        print("Only positive amounts are allowed.")
        return

    expense_a = {"Description": description, "Amount": amount}
    expenses.append(expense_a)


def remove_expense(description):
    for exp in expenses:
        if exp["Description"] == description:
            expenses.remove(exp)
            return True
    return False


def list_expenses():
    print("\nList of expenses:")
    for exp in expenses:
        print(f'{exp["Description"]}: ${exp["Amount"]}')


def calculate_total():
    total = 0
    for exp in expenses:
        total += exp["Amount"]
    return total

while True:
    print("\n1. Add Expense")
    print("2. Remove Expense")
    print("3. List of Expenses")
    print("4. Calculate Total Expenses")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    if choice == '1':
        desc = input("\nEnter expense description: ").title().strip()
        amt = float(input("Enter amount: "))
        add_expense(desc, amt)
    elif choice == '2':
        desc = input("\nEnter expense description to remove: ").title().strip()
        if remove_expense(desc):
            print(f"{desc} removed")
        else:
            print("Expense not found.")
    elif choice == '3':
        list_expenses()
    elif choice == '4':
        total = calculate_total()
        print(f"Total Expenses: ${total}")
    elif choice == '5':
        print("\nGoodbye!")
        break
    else:
        print("Invalid option, try again.")
