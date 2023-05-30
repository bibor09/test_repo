class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num

    def subtract(self, num):
        self.result -= num

    def multiply_by_result(self, num):
        self.result *= self.result * num

    def divide_by_result(self, num):
        if self.result != 0:
            self.result = num / self.result

    def print_result(self):
        print("Result:", self.result)


calculator = Calculator()

calculator.add(5)
calculator.subtract(2)
calculator.multiply_by_result(3)
calculator.divide_by_result(10)
calculator.print_result()
