from product import Product
from user import User
from cart import Cart
from premUser import PremiumUser

# Create products
laptop = Product("Laptop", 1500, 5)
mouse = Product("Mouse", 50, 10)

# Create users
alice = User("Alice")
bob = PremiumUser("Bob")

# Alice adds products
alice.cart.add_product(laptop, 1)
alice.cart.add_product(mouse, 1)
alice.cart.view_cart()
print(f"Alice's cart total: {alice.calculate_total()}")

# Bob adds products
bob.cart.add_product(mouse, 2)
bob.cart.view_cart()
print(f"Bob's cart total with discount: {bob.calculate_total()}")
