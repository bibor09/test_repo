class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"

    def fetch(self):
        return "Fetching a ball."


class Cat(Animal):
    def speak(self):
        return "Meow!"

    def scratch(self):
        return "Scratching the furniture."


class Bird(Animal):
    def speak(self):
        return "Chirp!"

    def fly(self):
        return "Flying in the sky."
    

class Parrot(Bird):
    def speak(self):
        return "Chirp!"

    def fly(self):
        return "Flying in the sky."
    
    def color(self):
        return "Red."


dog = Dog("Buddy")
print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof!
print(dog.fetch())  # Output: Fetching a ball.

# cat = Cat("Whiskers")
# print(cat.name)  # Output: Whiskers
# print(cat.speak())  # Output: Meow!
# print(cat.scratch())  # Output: Scratching the furniture.

