def count_ways(coins, amount, n):
    # Base case: exact amount achieved
    if amount == 0:
        return 1

    # If amount becomes negative or no coins left
    if amount < 0 or n == 0:
        return 0

    # Include current coin + Exclude current coin
    return count_ways(coins, amount - coins[n - 1], n) + \
           count_ways(coins, amount, n - 1)


# Coin values
coins = [1, 2, 5]

# Input amount
money = int(input("Enter the amount: "))

# Function call
ways = count_ways(coins, money, len(coins))

print("Number of ways to divide the money:", ways)