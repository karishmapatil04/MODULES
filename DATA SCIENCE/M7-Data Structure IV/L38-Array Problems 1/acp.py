# Input array
arr = [1, 2, 4, 5]  # Missing number is 3

n = len(arr) + 1  # because one number is missing

# Expected sum
expected_sum = n * (n + 1) // 2

# Actual sum
actual_sum = sum(arr)

# Missing number
missing_number = expected_sum - actual_sum

print("Missing Number:", missing_number)
