import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Display basic information about the DataFrame
print("\nDataFrame Info:")
print(df.info())

# Display descriptive statistics of the DataFrame
print("\nDescriptive Statistics:")
print(df.describe())

# Add a new column to the DataFrame
df['Gender'] = ['Female', 'Male', 'Male', 'Male', 'Female']
print("\nDataFrame after adding a new column:")
print(df)

# Filter the DataFrame to show individuals over 30
print("\nIndividuals over 30:")
print(df[df['Age'] > 30])

# Group by 'Gender' and calculate the average salary
print("\nAverage salary by Gender:")
print(df.groupby('Gender')['Salary'].mean())

# Save DataFrame to a CSV file
df.to_csv('data.csv', index=False)
print("\nDataFrame saved to 'data.csv'")
