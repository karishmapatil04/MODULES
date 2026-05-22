import pandas as pd

# Creating a sample dataset
data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan"],
    "Age": [20, 22, 21, 23, 24],
    "Marks": [85, 90, 78, 88, 95]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Display original data
print("Original Data:")
print(df)

# Display first 3 rows
print("\nFirst 3 Rows:")
print(df.head(3))

# Select specific column
print("\nNames Column:")
print(df["Name"])

# Add a new column
df["Result"] = ["Pass", "Pass", "Pass", "Pass", "Pass"]

print("\nData after adding new column:")
print(df)

# Filter data (Marks greater than 85)
print("\nStudents with Marks greater than 85:")
print(df[df["Marks"] > 85])

# Sorting data by Marks
print("\nData sorted by Marks:")
print(df.sort_values(by="Marks"))

# Calculate average marks
print("\nAverage Marks:", df["Marks"].mean())