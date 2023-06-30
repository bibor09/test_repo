class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

#     def fetch(self):
#         return "Fetching a ball."

class Horse(Animal):
    def speak(self):
        return "Nyihaha"


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

cat = Cat("Whiskers")
print(cat.name)  # Output: Whiskers
print(cat.speak())  # Output: Meow!
print(cat.scratch())  # Output: Scratching the furniture.

bird = Bird("Tweetie")
print(bird.name)  # Output: Tweetie
print(bird.speak())  # Output: Chirp!
print(bird.fly())  # Output: Flying in the sky.


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self):
        print(f"{self.name} is speaking.")

    def __str__(self):
        return f"{self.name} ({self.age} years old, {self.gender})"


class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

    def __str__(self):
        return f"{super().__str__()} - Student ID: {self.student_id}"


class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def __str__(self):
        return f"{super().__str__()} - Subject: {self.subject}"


# Creating instances of different person types
person1 = Person("John Doe", 30, "Male")
print(person1)
person1.speak()

student1 = Student("Alice Smith", 20, "Female", "S1234")
print(student1)
student1.speak()
student1.study()

teacher1 = Teacher("Mr. Johnson", 40, "Male", "Math")
print(teacher1)
teacher1.speak()
teacher1.teach()
