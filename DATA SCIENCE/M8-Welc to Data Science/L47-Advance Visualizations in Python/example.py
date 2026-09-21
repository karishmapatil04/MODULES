import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
df = df.dropna()

print(df.head())


# Point plot — average bill per day by gender with confidence intervals
sns.pointplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Bill per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill ($)')
plt.show()
# lmplot — scatter with fitted regression trend line
sns.lmplot(x='total_bill', y='tip', data=df)
plt.title('Total Bill vs Tip — Trend Line')
plt.show()