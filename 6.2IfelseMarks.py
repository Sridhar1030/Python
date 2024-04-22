# Enter 5 Subject Marks and Display Results (First, Second, Pass, Fail)
def subject_results():
    marks = []
    for i in range(5):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    total_marks = sum(marks)
    percentage = (total_marks / (len(marks) * 100)) * 100

    # Display results
    print("\nRESULTS:")
    print("Total Marks:", total_marks)
    print("Percentage of Marks:", percentage)

    # Check for result
    if all(mark >= 40 for mark in marks):
        print("Result: PASS")
        if percentage >= 60:
            print("Division: First")
        elif 50 <= percentage < 60:
            print("Division: Second")
        else:
            print("Division: Third")
    else:
        print("Result: FAIL")

# Call the function
subject_results()
