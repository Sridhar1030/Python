# Recursive function for the factorial of a given number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Main function
def main():
    number = int(input("Enter a number: "))
    print("Factorial of", number, "is", factorial(number))

# Call the main function
main()