# Add, Subtract, Multiply, and Divide Two Numbers
def arithmetic_operations():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Sum:", num1 + num2)
    print("Difference:", num1 - num2)
    print("Product:", num1 * num2)
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Division: Cannot divide by zero")

# Call the function
arithmetic_operations()
