import numpy as np

# Understanding various methods of the array class
def array_methods():
    # Create an array
    arr = np.array([1, 2, 3, 4, 5])
    print("Original Array:", arr)

    # Reshape the array
    arr_reshaped = arr.reshape(5, 1)
    print("Reshaped Array:")
    print(arr_reshaped)

    # Slicing the array
    print("Sliced Array:")
    print(arr[2:5])

    # Indexing the array
    print("Element at index 3:", arr[3])

    # Append elements to the array
    arr = np.append(arr, [6, 7])
    print("Array after append:", arr)

# Call the function
array_methods()




# NumPy arrays are better than normal arrays because they are:

# More Efficient: NumPy arrays are implemented in C, making them faster and more memory efficient than Python lists.

# Convenient: NumPy offers a wide range of mathematical functions and operations that are optimized for arrays.

# Easy to Use: NumPy simplifies array operations and manipulations, making it easier to work with large datasets and perform complex mathematical computations.