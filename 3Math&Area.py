import math

# Math functions: Power, Square root, and Factorial
def math_functions():
    print("Power of 2 to the power of 3:", math.pow(2, 3))
    print("Square root of 16:", math.sqrt(16))
    print("Factorial of 5:", math.factorial(5))

# Call math functions
math_functions()



def area(radius):
    return math.pi * radius ** 2

radius = float(input("Enter the radius of the circle: "))
print("Area of circle with radius", radius, "is", area(radius))
