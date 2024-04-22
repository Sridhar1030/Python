# Identity and Membership Operators

# Identity Operators: is, is not
def identity_operators(a, b):
    print("Identity Operators:")
    print("a is b:", a is b)       # Checks if a and b are the same object
    print("a is not b:", a is not b)   # Checks if a and b are not the same object
    print()

# Membership Operators: in, not in
def membership_operators(a, b):
    print("Membership Operators:")
    print("a in b:", a in b)       # Checks if a is a member of b
    print("a not in b:", a not in b)   # Checks if a is not a member of b
    print()

# Example usage
def main():
    x = 10
    y = 1
    identity_operators(x, y)

    lst = [1, 2, 3, 4, 5]
    a = 3
    membership_operators(a, lst)

if __name__ == "__main__":
    main()
