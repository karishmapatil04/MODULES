# 0-1 Knapsack Problem using Backtracking

def knapsack(weights, values, n, capacity, index, currentWeight, currentValue):
    # If all items are considered
    if index == n:
        return currentValue

    # Exclude current item
    exclude = knapsack(weights, values, n, capacity,
                       index + 1, currentWeight, currentValue)

    # Include current item (if possible)
    include = currentValue
    if currentWeight + weights[index] <= capacity:
        include = knapsack(weights, values, n, capacity,
                           index + 1,
                           currentWeight + weights[index],
                           currentValue + values[index])

    # Return maximum value
    return max(include, exclude)


# Main Program
n = int(input("Enter number of items: "))

weights = []
values = []

print("Enter weight and value of each item:")
for i in range(n):
    w = int(input(f"Weight of item {i+1}: "))
    v = int(input(f"Value of item {i+1}: "))
    weights.append(w)
    values.append(v)

capacity = int(input("Enter knapsack capacity: "))

maxValue = knapsack(weights, values, n, capacity, 0, 0, 0)

print("Maximum value in knapsack =", maxValue)