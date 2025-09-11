from user import User

class PremiumUser(User):
    def place_order(self):
        total = self.order.calculate_total()
        discounted_total = total * 0.85  # 15% discount
        print(f"{self.name}'s order total with discount: ${discounted_total:.2f}")
        self.last_ordered_item = self.order.items[-1].name if self.order.items else None

