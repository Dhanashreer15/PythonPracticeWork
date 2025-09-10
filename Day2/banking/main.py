from banking import accounts, transactions

accounts.create("Aarav", 5000)
accounts.create("Diya", 3000)

print("Aarav's Balance:", accounts.get_balance("Aarav"))
print("Diya's Balance:", accounts.get_balance("Diya"))

transactions.deposit("Aarav", 2000)

transactions.withdraw("Diya", 1000)
transactions.transfer("Aarav", "Diya", 1500)

print("Aarav's Final Balance:", accounts.get_balance("Aarav"))
print("Diya's Final Balance:", accounts.get_balance("Diya"))
