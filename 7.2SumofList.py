# Find the Sum of Integers Present in the List
def sum_of_integers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Main function
def main():
    numbers = [int(x) for x in input("Enter the numbers separated by space: ").split()]
    result = sum_of_integers(numbers)
    print("Sum of integers in the list:", result)

# Call the main function
main()
