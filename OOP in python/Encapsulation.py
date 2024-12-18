from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    def __init__(self, base, height):
        # Private attributes
        self.__base = base
        self.__height = height

    # Getter for base
    def get_base(self):
        return self.__base

    # Setter for base
    def set_base(self, base):
        if base > 0:  # Validating that the base is positive
            self.__base = base
        else:
            raise ValueError("Base must be a positive number")

    # Getter for height
    def get_height(self):
        return self.__height

    # Setter for height
    def set_height(self, height):
        if height > 0:  # Validating that the height is positive
            self.__height = height
        else:
            raise ValueError("Height must be a positive number")

    def calculate_area(self):
        pass  # Abstract method with no implementation


# Derived class
class Triangle(Shape):
    def calculate_area(self):
        # Using getters to access private attributes
        area = 0.5 * self.get_base() * self.get_height()
        print("The area of the Triangle is: " + str(area))


# Input values
base = float(input("Enter the base value: "))
height = float(input("Enter the height value: "))


triangle = Triangle(base, height)

# Accessing and modifying attributes through encapsulated methods
triangle.set_base(base) 
triangle.set_height(height)  

triangle.calculate_area()
