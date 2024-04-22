# Print Prime Numbers Up to a Given Number
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

def print_primes(n):
    print(f"Prime numbers up to {n}:")
    for num in range(2, n + 1):
        if is_prime(num):
            print(num, end=" ")

# Main function
def main():
    n = int(input("Enter the number (n): "))
    print_primes(n)

# Call the main function
main()
