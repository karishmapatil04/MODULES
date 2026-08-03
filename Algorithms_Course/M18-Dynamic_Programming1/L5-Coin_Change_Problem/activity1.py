def coin_change(coins, amount):
    # Initialize a table to store the minimum number of coins needed for each amount from 1 to the target.
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Solve subproblems for each amount from 1 to the target.
    for i in range(1, amount + 1):
        # Try using each coin denomination
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]

# Example usage
coins = [1, 2, 5]
amount = 11

result = coin_change(coins, amount)
print(f"The minimum number of coins needed: {result}")