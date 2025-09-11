
class Order:
    def __init__(self):
        self.items=[]

    def add_item(self, food_item):
        if food_item.available:
            self.items.append(food_item)
            print(f"Added '{food_item.name}' to the order.")
        else:
            print(f"'{food_item.name}' is not available.")

    def remove_item(self, food_item_name):
        for item in self.items:
            if item.name == food_item_name:
                self.items.remove(item)
                print(f"Removed '{food_item_name}' from the order.")
                return
        print(f"'{food_item_name}' not found in the order.")

    def calculate_total(self):
        return sum(item.price for item in self.items)

