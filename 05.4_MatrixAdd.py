import numpy as np

# Matrix Addition
def matrix_addition():
    # Define matrices
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])

    # Perform addition
    result_matrix = np.add(matrix1, matrix2)

    # Display result
    print("Matrix 1:")
    print(matrix1)
    print("\nMatrix 2:")
    print(matrix2)
    print("\nResultant Matrix (Matrix 1 + Matrix 2):")
    print(result_matrix)

# Call the function
matrix_addition()
