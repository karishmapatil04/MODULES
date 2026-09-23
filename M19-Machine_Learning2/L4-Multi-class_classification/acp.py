# Step 1: Import required libraries
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report

# Step 2: Create the dataset
# X contains the input features
X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [5, 6],
    [6, 7],
    [7, 8],
    [9, 10],
    [10, 11],
    [11, 12]
])

# y contains the target classes
y = np.array([
    0, 0, 0,
    1, 1, 1,
    2, 2, 2
])

# Step 3: Check the number of classes
print("Unique Classes:", np.unique(y))
print("Number of Classes:", len(np.unique(y)))

# Step 4: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# Step 5: Create the multi-class classification model
model = LogisticRegression(
    multi_class='multinomial',
    max_iter=1000
)

# Step 6: Train the model
model.fit(X_train, y_train)

# Step 7: Make predictions
y_pred = model.predict(X_test)

# Step 8: Display actual and predicted values
print("\nActual values:")
print(y_test)

print("\nPredicted values:")
print(y_pred)

# Step 9: Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

# Step 10: Display confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Step 11: Display classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Step 12: Predict a new observation
new_data = np.array([[4, 5]])

prediction = model.predict(new_data)

print("\nNew Input:", new_data)
print("Predicted Target Class:", prediction[0])