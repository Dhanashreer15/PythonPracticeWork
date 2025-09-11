# Cart class
class Cart:
    def __init__(self):
        self.items = {}  # product: quantity

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            product.stock -= quantity
            self.items[product] = self.items.get(product, 0) + quantity
            self.last_added_item = product.name  # dynamic attribute
            print(f"Added '{product.name}' to cart.")
        else:
            print(f"Not enough stock for '{product.name}'.")

    def remove_product(self, product):
        if product in self.items:
            product.stock += self.items[product]
            del self.items[product]
            print(f"Removed '{product.name}' from cart.")
        else:
            print(f"'{product.name}' not in cart.")

    def view_cart(self):
        print("Cart Items:")
        for product, qty in self.items.items():
            print(f"  {product.name} x {qty} = ₹{product.price * qty}")
        print(f"Last added item: {getattr(self, 'last_added_item', 'None')}")

    def calculate_total(self):
        return sum(product.price * qty for product, qty in self.items.items())



