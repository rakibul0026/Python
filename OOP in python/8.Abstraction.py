from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        pass  # Abstract method with no implementation

# Derived class
class Triangle(Shape):
    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print("The area of the Triangle is: " + str(area))


base = float(input("Enter the base value: "))
height = float(input("Enter the height value: "))

triangle = Triangle(base, height)
triangle.calculate_area()

