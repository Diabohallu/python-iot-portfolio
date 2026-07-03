
import atm2

print("\nWelcome to the ATM")
print("You can do the following")

while True:
    print("\n1.Deposit Amount")
    print("2.View Account")
    print("3.Withdraw Account")
    print("4.Exit")

    opt = input("Choose an option: ")

    if opt == "1":
        amount = float(input("How much amount would you like to deposit: "))
        print(atm2.add_amount(amount))

    elif opt == "2":
        print(atm2.account())

    elif opt == "3":
        amount = float(input("How much do you want to withdraw: "))
        print(atm2.withdraw(amount))

    elif opt == "4":
        print("Goodbye\n")
        break

    else:
        print("Invalid option, choose from one of the options\n")
        






