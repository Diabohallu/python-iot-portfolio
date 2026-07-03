balance = 0

def check_balance():
    print("Your balance is:", balance)

def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    balance = balance + amount
    print("Deposit successful!")
    print("New balance:", balance)

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful!")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance!")

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice! Please try again.")