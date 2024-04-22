# Convert octal to decimal
def octal_to_decimal(octal):
    decimal = 0
    power = 0
    while octal != 0:
        decimal += (octal % 10) * (8 ** power)
        octal //= 10
        power += 1
    return decimal

# Convert binary to decimal
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary != 0:
        decimal += (binary % 10) * (2 ** power)
        binary //= 10
        power += 1
    return decimal

# Convert hexadecimal to decimal
def hex_to_decimal(hexadecimal):
    decimal = 0
    power = 0
    for digit in str(hexadecimal)[::-1]:
        if digit.isdigit():
            decimal += int(digit) * (16 ** power)
        else:
            decimal += (ord(digit.upper()) - 55) * (16 ** power)
        power += 1
    return decimal
def main():
    choice = input("Enter the number system to convert to decimal (octal, binary, hexadecimal): ").lower()
    
    if choice == "octal":
        octal_number = int(input("Enter an octal number: "), 8)
        print("Octal to Decimal:", octal_to_decimal(octal_number))
    elif choice == "binary":
        binary_number = int(input("Enter a binary number: "), 2)
        print("Binary to Decimal:", binary_to_decimal(binary_number))
    elif choice == "hexadecimal":
        hexadecimal_number = int(input("Enter a hexadecimal number: "), 16)
        print("Hexadecimal to Decimal:", hex_to_decimal(hexadecimal_number))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
