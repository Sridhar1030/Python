import numpy as np

def calculate_marks():
    # Input marks
    marks = []
    for i in range(5):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    marks_array = np.array(marks)

    # Calculate total marks and percentage
    total_marks = np.sum(marks_array)
    percentage = (total_marks / (len(marks_array) * 100)) * 100

    # Display total marks and percentage
    print("Total Marks:", total_marks)
    print("Percentage of Marks:", percentage)

# Call the function
calculate_marks()
