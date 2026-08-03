def subset_sum(set_elements, target_sum):
    n = len(set_elements)

    # Initialize a 2D array to store the results of subproblems
    dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]

    # An empty subset always sums up to 0
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if set_elements[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - set_elements[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target_sum]

# Example usage:
set_elements = [3, 34, 4, 12, 5, 2]
target_sum = 9

if subset_sum(set_elements, target_sum):
    print("There is a subset with the target sum.")
else:
    print("There is no subset with the target sum.")