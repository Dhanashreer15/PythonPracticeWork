class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display_details(self):
        print(f"Product: {self.name}, Price: ₹{self.price}, Stock: {self.stock}")
