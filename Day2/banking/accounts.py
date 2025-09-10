accounts = {}

def create_account(name, initial_balance=0):
    accounts[name] = initial_balance
    print(f"Account created for {name} with balance {initial_balance}")

def get_balance(name):
    return accounts.get(name, "Account not found")
