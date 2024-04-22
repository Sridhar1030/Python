class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


def main():
    # Creating objects of the Rectangle class
    rect1 = Rectangle(5, 4)
    rect2 = Rectangle(7, 3)

    # Displaying the details of rectangle 1
    print("Rectangle 1:")
    print("Length:", rect1.length)
    print("Width:", rect1.width)
    print("Area:", rect1.area())
    print("Perimeter:", rect1.perimeter())
    print()

    # Displaying the details of rectangle 2
    print("Rectangle 2:")
    print("Length:", rect2.length)
    print("Width:", rect2.width)
    print("Area:", rect2.area())
    print("Perimeter:", rect2.perimeter())
    print()


if __name__ == "__main__":
    main()
