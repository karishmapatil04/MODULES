def is_palindrome(s):
    return s == s[::-1]

def palindromic_partitioning(s):
    n = len(s)
    dp = [float('inf')] * n

    for i in range(n):
        for j in range(i + 1):
            if is_palindrome(s[j:i + 1]):
                if j == 0:
                    dp[i] = 0
                else:
                    dp[i] = min(dp[i], dp[j - 1] + 1)

    return dp[n - 1]

# Example usage:
input_string = "aabcb"
min_partitions = palindromic_partitioning(input_string)
print("Minimum partitions needed:", min_partitions)