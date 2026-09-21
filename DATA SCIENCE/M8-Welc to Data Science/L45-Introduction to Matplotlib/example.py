import matplotlib.pyplot as plt

days   = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
scores = [70, 85, 60, 90, 75]

plt.bar(days, scores, color='orange')
plt.title('My Quiz Score Bar Chart')
plt.xlabel('Day of the Week')
plt.ylabel('Score')
plt.ylim(0, 100)
plt.show()