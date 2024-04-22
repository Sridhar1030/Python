import matplotlib.pyplot as plt
import numpy as np

# Line Plot
def line_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='sin(x)', color='blue')
    plt.title('Line Plot: sin(x)')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Bar Plot
def bar_plot():
    x = ['A', 'B', 'C', 'D', 'E']
    y = [23, 45, 56, 78, 33]

    plt.figure(figsize=(8, 5))
    plt.bar(x, y, color='green')
    plt.title('Bar Plot')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Scatter Plot
def scatter_plot():
    x = np.random.randn(100)
    y = np.random.randn(100)

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='red', alpha=0.6)
    plt.title('Scatter Plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

# Histogram
def histogram():
    data = np.random.randn(1000)

    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=30, color='orange', edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def main():
    print("1. Line Plot\n2. Bar Plot\n3. Scatter Plot\n4. Histogram")

    while True:
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            line_plot()
            break
        elif choice == '2':
            bar_plot()
            break
        elif choice == '3':
            scatter_plot()
            break
        elif choice == '4':
            histogram()
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
