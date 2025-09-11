from food import FoodItem
from user import User
from order import Order
from premUser import PremiumUser

if __name__ == "__main__":
    # Food items
    pizza=FoodItem("Pizza", 500)
    burger=FoodItem("Burger", 250)
    sushi=FoodItem("Sushi", 300, available=False)

    # Users
    john=User("John")
    emma=PremiumUser("Emma")

    # John orders
    john.order.add_item(pizza)
    john.order.add_item(sushi)  # Not available
    john.order.remove_item("Burger")  # Not in order
    john.place_order()

    # Emma orders
    emma.order.add_item(burger)
    emma.place_order()

    # Dynamic attribute check
    print(f"Last item John ordered: {john.last_ordered_item}")
    print(f"Last item Emma ordered: {emma.last_ordered_item}")
