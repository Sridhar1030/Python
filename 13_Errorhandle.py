def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Unsupported operand type(s) for /")
    else:
        print("Result:", result)
    finally:
        print("End of function")

def main():
    # Test divide function
    print("--- Test 1 ---")
    divide(10, 2)

    print("\n--- Test 2 ---")
    divide(10, 0)

    print("\n--- Test 3 ---")
    divide("10", 2)

if __name__ == "__main__":
    main()
