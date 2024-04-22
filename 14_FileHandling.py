import os

def create_file(filename):
    try:
        with open(filename, 'w') as file:
            print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

def write_to_file(filename, text):
    try:
        with open(filename, 'a') as file:
            file.write(text + "\n")
            print("Text added to the file successfully.")
    except Exception as e:
        print(f"Error: {e}")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def print_unique_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
            unique_words = sorted(set(words))
            print("Unique words in alphabetical order:")
            for word in unique_words:
                print(word)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def main():
    filename = "test.txt"
    
    while True:
        print("\nOptions:")
        print("1. Create a file")
        print("2. Write to the file")
        print("3. Read and print unique words from the file")
        print("4. Delete the file")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            create_file(filename)
        elif choice == '2':
            text = input("Enter the text to write into the file: ")
            write_to_file(filename, text)
        elif choice == '3':
            print_unique_words(filename)
        elif choice == '4':
            delete_file(filename)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
