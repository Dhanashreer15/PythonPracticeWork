cart= []

def add(item,price):
    cart.append((item, price))

def remove(item):
    global cart
    cart=[i for i in cart if i[0]!= item]

def total():
    return sum(price for _, price in cart)
