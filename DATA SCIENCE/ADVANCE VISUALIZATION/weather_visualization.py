import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks")

# Correct CSV link
weather = pd.read_csv('https://docs.google.com/spreadsheets/d/19DuqMX-N6nDUnLMsYn_1EojQJhIfdZT98NJfWZTR9nA/export?format=csv')

print(weather.head())
print(weather.info())

# Barplot
sns.barplot(data=weather, x='humidity', y='temperature')
plt.show()

# Histogram (replacement for distplot)
sns.histplot(weather['humidity'], kde=True)
plt.show()

sns.histplot(weather['humidity'], kde=False)
plt.show()

# Joint plots
sns.jointplot(data=weather, x='humidity', y='temperature')
plt.show()

sns.jointplot(data=weather, x='humidity', y='temperature', kind="hex")
plt.show()

sns.jointplot(data=weather, x='humidity', y='temperature', kind="kde")
plt.show()

# Pairplot
sns.pairplot(weather[['humidity', 'temperature', 'air_pollution_index']])
plt.show()

# Stripplot
sns.stripplot(data=weather, x='weather_type', y='temperature')
plt.show()

sns.stripplot(data=weather, x='weather_type', y='temperature', jitter=True)
plt.show()

# Swarmplot (fixed)
sns.swarmplot(data=weather, x='weather_type', y='temperature')
plt.show()

# Barplot with hue
sns.barplot(data=weather, x='humidity', y='temperature', hue='weather_type')
plt.show()

# Countplot
sns.countplot(data=weather, x='weather_type')
plt.show()

# Pointplot
sns.pointplot(data=weather, x='humidity', y='temperature', hue='weather_type')
plt.show()