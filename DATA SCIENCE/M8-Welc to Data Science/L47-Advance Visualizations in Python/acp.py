import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Creating sample dataset
data = {
    'Student': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Karan', 'Riya', 'Arjun'],
    'Marks': [85, 90, 78, 88, 95, 82, 91],
    'Age': [20, 21, 19, 22, 20, 21, 23],
    'Study_Hours': [3, 5, 2, 4, 6, 3, 5]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Display dataset
print(df)

# Pair Plot
sns.pairplot(df)
plt.show()

# Heatmap (Correlation Matrix)
plt.figure(figsize=(6, 4))
correlation = df[['Marks', 'Age', 'Study_Hours']].corr()
sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.show()

# Violin Plot
plt.figure(figsize=(6, 4))
sns.violinplot(y=df['Marks'])
plt.title("Marks Distribution - Violin Plot")
plt.show()

# Swarm Plot
plt.figure(figsize=(6, 4))
sns.swarmplot(y=df['Marks'])
plt.title("Marks Distribution - Swarm Plot")
plt.show()

# Regression Plot
plt.figure(figsize=(6, 4))
sns.regplot(x='Study_Hours', y='Marks', data=df)
plt.title("Study Hours vs Marks")
plt.show()