
expenses = []


def save():
    with open("expenses.txt", "a") as file:
        for expense in expenses:
            file.write(f'{expense["description"]}: ${expense["amount"]}\n')


def add(description, amount):
    if amount <= 0:
        return "Amount must be greater than 0."
    expenses.append({"description": description, "amount": amount})
    save()
    return f"Added {description}."


def remove(description):
    for expense in expenses:
        if expense["description"].lower() == description.lower():
            expenses.remove(expense)
            save()
            return f"Removed {description}."
        
    return f"{description} was not found."


def list():
    if (expenses == ""):
        return "No expences added"
    
    return [f"{expense["description"]}: ${expense["amount"]:.2f}" for expense in expenses]


def calculate():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

    