import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
data = pd.read_csv(r'C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\MACHINE_LEARNING\Legendary pokemon prediction\Pokemon Data.csv')

# Display first 5 rows
print(data.head())

# Fill missing values in Type 2
data['Type 2'].fillna(value='None', inplace=True)

# Check for missing values
print(data.isnull().sum())

# Visualizations
data['Type 1'].value_counts().plot.bar()
plt.title('Type 1 Distribution')
plt.show()

data['Type 2'].value_counts().plot.bar()
plt.title('Type 2 Distribution')
plt.show()

data['Legendary'].value_counts().plot.bar()
plt.title('Legendary Distribution')
plt.show()

# Display unique values
print(data['Type 1'].unique())
print(data['Type 2'].unique())

# Encode target column
from sklearn.preprocessing import LabelEncoder

lb = LabelEncoder()
data['Legendary'] = lb.fit_transform(data['Legendary'])

# Remove Name column
data.drop('Name', axis=1, inplace=True)

# Convert categorical columns to numerical
data = pd.get_dummies(data)

print("Dataset Shape:", data.shape)

# Separate features and target
X = data.drop('Legendary', axis=1)
y = data['Legendary']

# Train-Test Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42
)

# -----------------------------------
# Logistic Regression
# -----------------------------------
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

LogReg = LogisticRegression(max_iter=1000)

LogReg.fit(X_train, y_train)

ypred1 = LogReg.predict(X_test)

print("Logistic Regression Accuracy:",
      accuracy_score(y_test, ypred1))

# -----------------------------------
# KNN - Finding Best K
# -----------------------------------
from sklearn.neighbors import KNeighborsClassifier

error_rates = []

for k in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    error_rates.append(np.mean(preds != y_test))

# Plot Error Rate
plt.figure(figsize=(10, 7))

plt.plot(
    range(1, 40),
    error_rates,
    linestyle='dashed',
    marker='o',
    markersize=8
)

plt.title('Error Rate vs K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.grid(True)

plt.show()

# -----------------------------------
# Final KNN Model
# -----------------------------------
knn_model = KNeighborsClassifier(n_neighbors=8)

knn_model.fit(X_train, y_train)

y_predict = knn_model.predict(X_test)

print("KNN Accuracy:",accuracy_score(y_test, y_predict))

# -----------------------------------
# Decision Tree
# -----------------------------------
from sklearn.tree import DecisionTreeClassifier

clf_model = DecisionTreeClassifier(random_state=42)

clf_model.fit(X_train, y_train)

y_predict = clf_model.predict(X_test)

print("Decision Tree Accuracy:", accuracy_score(y_test, y_predict))