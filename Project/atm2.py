balance = 0.0

def add_amount(amount):
    global balance
    amount = float(amount)
    balance += amount
    return f"Deposited ${amount:.2f}. Current balance: ${balance:.2f}"


def withdraw(amount):
    global balance
    amount = float(amount)

    if amount > balance:
        return f"Insufficient balance. Current balance: ${balance:.2f}"

    balance -= amount
    return f"Withdrew ${amount:.2f}. Current balance: ${balance:.2f}"


def account():
    return f"Current balance: ${balance:.2f}"