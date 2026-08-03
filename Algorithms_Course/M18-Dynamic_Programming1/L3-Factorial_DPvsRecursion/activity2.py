def factorial_dp(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = i * dp[i - 1]

    return dp[n]

# Example usage
n = 5
result = factorial_dp(n)
print(f"The factorial of {n} is: {result}")