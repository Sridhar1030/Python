# Function to return multiple results (addition, subtraction, multiplication, and division)
def arithmetic_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Cannot divide by zero"
    return addition, subtraction, multiplication, division

# Main function
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    add, sub, mul, div = arithmetic_operations(num1, num2)
    print("Addition:", add)
    print("Subtraction:", sub)
    print("Multiplication:", mul)
    print("Division:", div)

# Call the main function
main()
