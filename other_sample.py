'''
In this sample code, we have a hierarchy of classes representing different shapes: 
Shape, Circle, Rectangle, and Triangle. The Shape class is the base class, and the other classes inherit from it.
 Each shape class has its own implementation of the area method. We also have a function calculate_total_area that 
 calculates the total area by iterating over a list of shapes.
'''

class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def calculate_total_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area


# Create shapes
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)
triangle = Triangle("Green", 3, 8)

# Get color of shapes
print("Circle color:", circle.get_color())
print("Rectangle color:", rectangle.get_color())
print("Triangle color:", triangle.get_color())

# Calculate areas
print("Circle area:", circle.area())
print("Rectangle area:", rectangle.area())
print("Triangle area:", triangle.area())

# Calculate total area
shapes = [circle, rectangle, triangle]
total_area = calculate_total_area(shapes)
print("Total area:", total_area)