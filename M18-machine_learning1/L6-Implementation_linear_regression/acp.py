import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Create sample data
# -----------------------------
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
y = np.array([2, 4, 5, 4, 5, 7, 8, 9, 10, 12], dtype=float)

# Number of data points
n = len(X)

# -----------------------------
# Step 2: Initialize parameters
# -----------------------------
m = 0       # Slope
b = 0       # Intercept

learning_rate = 0.01
epochs = 1000

# Store cost values
cost_history = []

# -----------------------------
# Step 3: Gradient Descent
# -----------------------------
for i in range(epochs):

    # Prediction
    y_pred = m * X + b

    # Calculate error
    error = y_pred - y

    # Calculate gradients
    dm = (2 / n) * np.sum(X * error)
    db = (2 / n) * np.sum(error)

    # Update parameters
    m = m - learning_rate * dm
    b = b - learning_rate * db

    # Calculate Mean Squared Error
    cost = np.mean(error ** 2)
    cost_history.append(cost)

# -----------------------------
# Step 4: Display results
# -----------------------------
print("Slope (m):", m)
print("Intercept (b):", b)

print("Regression Equation:")
print(f"y = {m:.2f}x + {b:.2f}")

# -----------------------------
# Step 5: Plot regression line
# -----------------------------
plt.scatter(X, y, label="Actual Data")

y_pred = m * X + b
plt.plot(X, y_pred, label="Regression Line")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression using Gradient Descent")
plt.legend()
plt.show()

# -----------------------------
# Step 6: Plot cost function
# -----------------------------
plt.plot(range(epochs), cost_history)

plt.xlabel("Epochs")
plt.ylabel("Mean Squared Error")
plt.title("Cost Function vs Epochs")
plt.show()