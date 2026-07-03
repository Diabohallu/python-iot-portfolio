
expense_name = input("\nEnter where/what you spent your money in/on: ").title().strip().replace(" ",", ").split(",")
name_con = input("Is there any Expense left (yes/no): ")
while (name_con == "yes"):
    update_name = input("Do you wanna update (add/remove/no): ")
    if (update_name == "add"):
        add_name = input("What do you wanna add: ")
        expense_name.append(add_name)
    elif (update_name == "remove"):
        remove_name = input("What do you wanna remove: ")
        expense_name.remove(remove_name)
    elif (update_name == "no"):
        break
       
expense_amount = input("Enter how much you spent on each: ").strip().replace(" ",", ").split(",")
amount_con = input("Is there any Amount left (yes/no): ")
while (amount_con == "yes"):
    update_amount = input("Do you wanna update (add/remove/no): ")
    if (update_amount == "add"):
        add_amount = input("What do you wanna add: ").strip().replace(" ",", ")
        expense_amount.append(add_amount)
    elif (update_amount == "remove"):
        remove_amount = input("What do you wanna remove: ").strip().replace(" ",", ")
        expense_amount.remove(remove_amount)
    elif (update_amount == "no"):
        break

if (len(expense_name) != len(expense_amount)):
    print("Number of Expences does not match Number of Payment Amounts")
    name_con = input("Is there any Expense left (yes/no): ")
    while (name_con == "yes"):
        update_name = input("Do you wanna update Expense (add/remove/no): ")
        if (update_name == "add"):
            add_name = input("What do you wanna add: ").strip().replace(" ",", ")
            expense_name.append(add_name)
        elif (update_name == "remove"):
            remove_name = input("What do you wanna remove: ").strip().replace(" ",", ")
            expense_name.remove(remove_name)
        elif (update_name == "no"):
             break
       
    amount_con = input("Is there any Amount name left (yes/no): ")
    while (amount_con == "yes"):
        update_amount = input("Do you wanna update  (add/remove/no): ")
        if (update_amount == "add"):
            add_amount = input("What do you wanna add: ").strip().replace(" ",", ")
            expense_amount.append(add_amount)
        elif (update_amount == "remove"):
            remove_amount = input("What do you wanna remove: ").strip().replace(" ",", ")
            expense_amount.remove(remove_amount)
        elif (update_amount == "no"):
            break

print("\nThings Expenses were spent at: ", str(expense_name))
print("Amount of Expenses spent:", str(expense_amount))



print("\nInformation on Expenses:")

expense = {
    "Expense": expense_name,
    "Amount": expense_amount
}

for key, value in expense.items():
    print(key,":","$",value)