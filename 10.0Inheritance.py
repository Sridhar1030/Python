class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


def main():
    # Creating objects of the Rectangle class
    rect = Rectangle(5, 4)
    print("Rectangle:")
    print("Name:", rect.name)
    print("Length:", rect.length)
    print("Width:", rect.width)
    print("Area:", rect.area())
    print("Perimeter:", rect.perimeter())
    print()

    # Creating objects of the Circle class
    circle = Circle(7)
    print("Circle:")
    print("Name:", circle.name)
    print("Radius:", circle.radius)
    print("Area:", circle.area())
    print("Perimeter:", circle.perimeter())
    print()


if __name__ == "__main__":
    main()