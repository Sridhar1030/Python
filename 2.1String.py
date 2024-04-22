# String Operations
def string_operations():
    my_string = "Hello, World!"
    print("Original String:", my_string)

    # Display 0th character
    print("First character:", my_string[0])

    # Display 3rd to 6th character
    print("Characters from 3rd to 6th:", my_string[3:7])

    # Display 6th character onwards
    print("Characters from 6th onwards:", my_string[6:])

    # Display last character
    print("Last character:", my_string[-1])

    # Print the string twice
    print("String twice:", my_string * 2)

    # Concatenate two strings
    second_string = " Have a nice day!"
    print("Concatenated string:", my_string + second_string)

# Call the function
string_operations()
