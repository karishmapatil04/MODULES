def knapsack_01(weights, values, capacity):
    n = len(weights)

    # Initialize a 2D array to store the maximum values for subproblems
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):

            if weights[i - 1] <= j:
                # Decide whether to include the item or not
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
            else:
                # If the current item's weight exceeds the current capacity, exclude the item
                dp[i][j] = dp[i - 1][j]

    # The final result is stored in dp[n][capacity]
    max_value = dp[n][capacity]

    # Backtrack to find the items included in the knapsack
    items_in_knapsack = []
    j = capacity
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            items_in_knapsack.append(i - 1)
            j -= weights[i - 1]

    return max_value, items_in_knapsack[::-1]

# Example usage:
weights = [2, 3, 4, 5]  # List of weights of items
values = [3, 4, 5, 6]  # List of values of items
capacity = 5  # Maximum weight capacity of the knapsack

max_value, items_in_knapsack = knapsack_01(weights, values, capacity)
print("Maximum value in knapsack:", max_value)
print("Items included in the knapsack:", items_in_knapsack)
