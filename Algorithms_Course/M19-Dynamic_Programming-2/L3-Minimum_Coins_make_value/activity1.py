def min_coins(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for coin in coins:
        for val in range(coin, target + 1):
            dp[val] = min(dp[val], dp[val - coin] + 1)

    return dp[target]

# Example usage:
coins = [1, 2, 5]
target_value = 11
min_coins_needed = min_coins(coins, target_value)
print("Minimum number of coins needed:", min_coins_needed)