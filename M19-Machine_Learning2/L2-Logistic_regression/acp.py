# Step 1: Import required libraries
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Step 2: Create the given arrays
# Replace these values with the arrays given in your assignment

x = np.array([0, 0, 0, 1, 1, 1])
y = np.array([1, 2, 3, 6, 7, 8])

# Step 3: Reshape the input data
# Machine learning models expect X in 2D format

Y = y.reshape(-1, 1)

# Step 4: Split the data into training and testing sets
Y_train, Y_test, x_train, x_test = train_test_split(
    Y, x, test_size=0.2, random_state=42
)

# Step 5: Create the Logistic Regression model
model = LogisticRegression()

# Step 6: Train the model
model.fit(Y_train, x_train)

# Step 7: Predict x values using y values
x_pred = model.predict(Y_test)

# Step 8: Display predictions
print("Actual x values:", x_test)
print("Predicted x values:", x_pred)

# Step 9: Calculate accuracy
accuracy = accuracy_score(x_test, x_pred)

print("Accuracy:", accuracy)

# Step 10: Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(x_test, x_pred))

# Step 11: Predict x for a new y value
new_y = np.array([[5]])

prediction = model.predict(new_y)

print("\nFor y =", new_y[0][0])
print("Predicted x =", prediction[0])