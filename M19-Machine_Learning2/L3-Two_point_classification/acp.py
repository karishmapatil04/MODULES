# Step 1: Import required libraries
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 2: Create the dataset
# Replace these values with the given values in your assignment

x = np.array([0, 0, 0, 0, 1, 1, 1, 1])
y = np.array([1, 2, 3, 4, 6, 7, 8, 9])

# Step 3: Convert y into a 2D array
Y = y.reshape(-1, 1)

# Step 4: Split the dataset into training and testing data
Y_train, Y_test, x_train, x_test = train_test_split(
    Y, x, test_size=0.25, random_state=42
)

# Step 5: Create the Binary Classification model
model = LogisticRegression()

# Step 6: Train the model
model.fit(Y_train, x_train)

# Step 7: Predict x using y
x_pred = model.predict(Y_test)

# Step 8: Display actual and predicted values
print("Actual x values:")
print(x_test)

print("\nPredicted x values:")
print(x_pred)

# Step 9: Calculate accuracy
accuracy = accuracy_score(x_test, x_pred)

print("\nAccuracy:", accuracy)

# Step 10: Display confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(x_test, x_pred))

# Step 11: Display classification report
print("\nClassification Report:")
print(classification_report(x_test, x_pred))

# Step 12: Predict x for a new y value
new_y = np.array([[5]])

prediction = model.predict(new_y)

print("\nFor y =", new_y[0][0])
print("Predicted x =", prediction[0])

# Step 13: Plot the data
plt.scatter(y, x)

plt.xlabel("y")
plt.ylabel("x")
plt.title("Binary Classification: Predicting x using y")

plt.show()