from ecommerce import cart, payment

cart.add("Shoes", 2500)
cart.add("Bag", 1500)

total = cart.total()
print(f"Total bill: {total}")
payment.payment(total)
