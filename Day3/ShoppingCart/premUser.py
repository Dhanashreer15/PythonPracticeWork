from user import User

class PremiumUser(User):
    def calculate_total(self):
        total = self.cart.calculate_total()
        discount = total * 0.10
        return total - discount