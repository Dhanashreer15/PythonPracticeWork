from banking import accounts

def deposit(name, amount):
    if name in accounts.accounts:
        accounts.accounts[name] += amount
        print(f"{amount} deposited to {name} account.")
        return True
    print("Account not found.")
    return False

def withdraw(name, amount):
    if name in accounts.accounts:
        if accounts.accounts[name] >= amount:
            accounts.accounts[name] -= amount
            print(f"{amount} withdrawn from {name} account.")
            return True
        else:
            print("Insufficient balance.")
            return False
    print("Account not found.")
    return False

def transfer(sender, receiver, amount):
    if withdraw(sender, amount):
        return deposit(receiver, amount)
    print("Transfer failed.")
    return False
