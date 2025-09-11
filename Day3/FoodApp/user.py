from order import Order
class User:
    def __init__(self, name):
        self.name=name
        self.order=Order()

    def place_order(self):
        total=self.order.calculate_total()
        print(f"{self.name}'s order total: ${total}")
        self.last_ordered_item = self.order.items[-1].name if self.order.items else None
