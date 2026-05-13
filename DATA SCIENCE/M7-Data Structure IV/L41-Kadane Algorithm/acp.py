# Input array
arr = [5, 10, 20, 6, 3, 8]

# Initialize
max_len = 1
current_len = 1

# Traverse array
for i in range(1, len(arr)):
    # Check alternating condition
    if (arr[i] % 2 == 0 and arr[i-1] % 2 != 0) or \
       (arr[i] % 2 != 0 and arr[i-1] % 2 == 0):
        current_len += 1
        max_len = max(max_len, current_len)
    else:
        current_len = 1

print("Longest Odd-Even Subarray Length:", max_len)