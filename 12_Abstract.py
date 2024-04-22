from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Interface
class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Rectangle(Shape, Printable):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def print_info(self):
        print(f"Rectangle - Length: {self.length}, Width: {self.width}, Area: {self.area()}, Perimeter: {self.perimeter()}")


class Circle(Shape, Printable):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

    def print_info(self):
        print(f"Circle - Radius: {self.radius}, Area: {self.area()}, Perimeter: {self.perimeter()}")


def main():
    rect = Rectangle(5, 4)
    circle = Circle(7)

    rect.print_info()
    circle.print_info()


if __name__ == "__main__":
    main()
    

# Abstract class
# An abstract class is a class that is designed to be inherited by other classes. It contains one or more abstract methods.
# Abstract methods are declared, but they do not contain any implementation. 
# The implementation of these methods is provided by the subclass.
# Abstract classes cannot be instantiated, and any class that contains one or more abstract methods must also be abstract.

# Interface
# An interface in Python is an abstract base class that only contains abstract methods.
# It is used to define a protocol of methods that can be used by any class, regardless of its hierarchy.
# Interfaces allow multiple inheritances, meaning that a class can inherit from multiple interfaces.
# In Python, interfaces are created using abstract classes, and the abc (Abstract Base Classes) module provides the infrastructure for defining Abstract Base Classes (ABCs) in Python.
