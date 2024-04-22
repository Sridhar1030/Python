# Check Whether the Entered Number is Even or Odd
def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

# Main function
def main():
    number = int(input("Enter a number: "))
    check_even_odd(number)

# Call the main function
main()
