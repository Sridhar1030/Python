# # Range
# def range_operation():
#     my_range = range(5, 10)
#     print("Range:", list(my_range))

# # Call the function
# range_operation()



# Range Operations

# Function to demonstrate range operations
def range_operations():
    # Example 1: Range with one argument (stop)
    print("Example 1: Range with one argument (stop)")
    for i in range(5):
        print(i, end=' ')
    print("\n")

    # Example 2: Range with two arguments (start, stop)
    print("Example 2: Range with two arguments (start, stop)")
    for i in range(5, 10):
        print(i, end=' ')
    print("\n")

    # Example 3: Range with three arguments (start, stop, step)
    print("Example 3: Range with three arguments (start, stop, step)")
    for i in range(0, 10, 2):
        print(i, end=' ')
    print("\n")

    # Example 4: Range with negative step
    print("Example 4: Range with negative step")
    for i in range(10, 0, -2):
        print(i, end=' ')
    print("\n")

# Call the function
range_operations()
