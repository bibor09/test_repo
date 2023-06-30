import random

class Calculate():
    def __init__(self):
        self.random = Random()
        self.avg = Average()

class Random():
    def generate_random_numbers(self):
        numbers = []
        for _ in range(10):
            numbers.append(random.randint(1, 100))
        return numbers

class Average():
    def calculate_average(numbers):
        total = sum(numbers)
        average = total / len(numbers)
        return average
    
class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []

    def add_item(self, item):
        self.items.append(item)


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)


class Item:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price


# Creating instances of classes
customer1 = Customer(1, "John Doe")
item1 = Item(1, "Shirt", 25.99)
order1 = Order(1, customer1)

# Establishing efferent coupling
customer1.place_order(order1)
order1.add_item(item1)

# Accessing afferent coupling
for order in customer1.orders:
    print(f"Order ID: {order.order_id}")
    for item in order.items:
        print(f"Item ID: {item.item_id}, Name: {item.name}, Price: {item.price}")