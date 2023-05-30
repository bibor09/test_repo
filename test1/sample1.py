import random

def generate_random_numbers():
    numbers = []
    for _ in range(10):
        numbers.append(random.randint(1, 100))
    return numbers

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

def print_results(numbers, average):
    print("Random Numbers:")
    for num in numbers:
        print(num)
    print("Average:", average)

numbers = generate_random_numbers()
average = calculate_average(numbers)
print_results(numbers, average)
