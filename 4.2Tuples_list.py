# List and Tuple input
def input_list_tuple():
    # List input
    my_list = input("Enter elements of a list separated by space: ").split()
    print("List:", my_list)

    # Tuple input
    my_tuple = tuple(input("Enter elements of a tuple separated by space: ").split())
    print("Tuple:", my_tuple)

# Call the function
input_list_tuple()
