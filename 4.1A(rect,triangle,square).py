import math

# Function to calculate the area of a triangle
def triangle_area(base, height):
    return 0.5 * base * height

# Function to calculate the area of a circle
def circle_area(radius):
    return math.pi * radius ** 2

# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

# Main function
def main():
    # Triangle
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print("Area of the triangle:", triangle_area(base, height))

    # Circle
    radius = float(input("Enter the radius of the circle: "))
    print("Area of the circle:", circle_area(radius))

    # Rectangle
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print("Area of the rectangle:", rectangle_area(length, width))

if __name__ == "__main__":
    main()
