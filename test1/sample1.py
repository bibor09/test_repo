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
    

