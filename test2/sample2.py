class ExampleClass:
    def method1(self):
        print("Method 1")
        self.method2()

    def method2(self):
        print("Method 2")
        self.method3()

    def method3(self):
        print("Method 3")
        # Perform some operations
        self.method4()

# Create an instance of the class
example = ExampleClass()
example.method1()

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def honk(self):
        print("Honk!")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def drive(self):
        print(f"The {self.brand} {self.model} is driving.")

    def __str__(self):
        return f"{super().__str__()} - {self.fuel_type} fuel"


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year, "Electric")
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"The {self.brand} {self.model} is charging.")

    def __str__(self):
        return f"{super().__str__()} - {self.battery_capacity} kWh battery"


class HybridCar(Car):
    def __init__(self, brand, model, year, fuel_type, battery_capacity):
        super().__init__(brand, model, year, fuel_type)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"The {self.brand} {self.model} is charging.")

    def drive(self):
        print(f"The {self.brand} {self.model} is driving in hybrid mode.")

    def __str__(self):
        return f"{super().__str__()} - {self.fuel_type}/{self.battery_capacity} kWh battery"


# Creating instances of different car types
car1 = Car("Toyota", "Corolla", 2022, "Petrol")
print(car1)
car1.honk()
car1.drive()

electric_car1 = ElectricCar("Tesla", "Model S", 2023, 85)
print(electric_car1)
electric_car1.honk()
electric_car1.drive()
electric_car1.charge()

hybrid_car1 = HybridCar("Toyota", "Prius", 2023, "Petrol", 2.4)
print(hybrid_car1)
hybrid_car1.honk()
hybrid_car1.drive()
hybrid_car1.charge()
