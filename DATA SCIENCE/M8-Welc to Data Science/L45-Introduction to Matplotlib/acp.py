import matplotlib.pyplot as plt
import pandas as pd

# Creating sample dataset
data = {
    'Student': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Karan'],
    'Marks': [85, 90, 78, 88, 95],
    'Age': [20, 21, 19, 22, 20]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Display dataset
print(df)

# Line Plot
plt.figure(figsize=(6, 4))
plt.plot(df['Student'], df['Marks'], marker='o')
plt.title("Student Marks - Line Plot")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Bar Chart
plt.figure(figsize=(6, 4))
plt.bar(df['Student'], df['Marks'])
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Pie Chart
plt.figure(figsize=(6, 4))
plt.pie(df['Marks'], labels=df['Student'], autopct='%1.1f%%')
plt.title("Marks Distribution")
plt.show()

# Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(df['Age'], df['Marks'])
plt.title("Age vs Marks - Scatter Plot")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()

# Histogram
plt.figure(figsize=(6, 4))
plt.hist(df['Marks'])
plt.title("Marks Distribution - Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()