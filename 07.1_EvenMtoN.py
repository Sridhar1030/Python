# Display Even Numbers from n to m
def display_even_numbers(n, m):
    print(f"Even numbers from {n} to {m}:")
    for num in range(n, m+1):
        if num % 2 == 0:
            print(num, end=" ")

# Main function
def main():
    n = int(input("Enter the starting number (n): "))
    m = int(input("Enter the ending number (m): "))
    display_even_numbers(n, m)

# Call the main function
main()
