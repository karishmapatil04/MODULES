import seaborn as sns
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

# Bar Plot
plt.figure(figsize=(6, 4))
sns.barplot(x='Student', y='Marks', data=df)
plt.title("Student Marks - Bar Plot")
plt.show()

# Line Plot
plt.figure(figsize=(6, 4))
sns.lineplot(x='Student', y='Marks', data=df, marker='o')
plt.title("Student Marks - Line Plot")
plt.show()

# Scatter Plot
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Age', y='Marks', data=df)
plt.title("Age vs Marks - Scatter Plot")
plt.show()

# Histogram
plt.figure(figsize=(6, 4))
sns.histplot(df['Marks'], kde=True)
plt.title("Marks Distribution")
plt.show()

# Box Plot
plt.figure(figsize=(6, 4))
sns.boxplot(y='Marks', data=df)
plt.title("Marks Box Plot")
plt.show()