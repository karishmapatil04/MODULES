# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating sample dataset
data = {
    'Student': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Karan', 'Riya'],
    'Age': [20, 21, 19, 22, 20, 23],
    'Marks': [85, 90, 78, 88, 95, 82],
    'Study_Hours': [3, 5, 2, 4, 6, 3]
}

# Creating DataFrame using Pandas
df = pd.DataFrame(data)

# Display Dataset
print("Dataset:")
print(df)

# ---------------- NUMPY OPERATIONS ----------------
print("\nNumPy Operations")

marks_array = np.array(df['Marks'])

print("Marks Array:", marks_array)
print("Average Marks:", np.mean(marks_array))
print("Maximum Marks:", np.max(marks_array))
print("Minimum Marks:", np.min(marks_array))
print("Standard Deviation:", np.std(marks_array))

# ---------------- PANDAS OPERATIONS ----------------
print("\nPandas Operations")

# Display first 3 rows
print("\nFirst 3 Rows:")
print(df.head(3))

# Filtering students with marks above 85
print("\nStudents with Marks > 85:")
print(df[df['Marks'] > 85])

# Sorting data by Marks
print("\nSorted by Marks:")
print(df.sort_values(by='Marks'))

# ---------------- MATPLOTLIB VISUALIZATION ----------------

# Line Plot
plt.figure(figsize=(6, 4))
plt.plot(df['Student'], df['Marks'], marker='o')
plt.title("Student Marks - Line Plot")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

# Bar Plot
plt.figure(figsize=(6, 4))
plt.bar(df['Student'], df['Marks'])
plt.title("Student Marks - Bar Plot")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

# ---------------- SEABORN VISUALIZATION ----------------

# Scatter Plot
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Study_Hours', y='Marks', data=df)
plt.title("Study Hours vs Marks")
plt.show()

# Heatmap
plt.figure(figsize=(6, 4))
correlation = df[['Age', 'Marks', 'Study_Hours']].corr()
sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.show()