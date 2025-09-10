import random

def payment(amount):
    print(f"Processing payment of {amount:.2f}...")
    success = random.choice([True, False])
    if success:
        print("Payment successful")
    else:
        print("Payment failed")
    return success
