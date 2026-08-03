def min_jumps(nums):
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            if j + nums[j] >= i:  # Check if it's possible to reach index i from index j
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[n - 1]

# Example usage:
nums = [2, 3, 1, 1, 4]
min_jumps_needed = min_jumps(nums)
print("Minimum number of jumps needed:", min_jumps_needed)