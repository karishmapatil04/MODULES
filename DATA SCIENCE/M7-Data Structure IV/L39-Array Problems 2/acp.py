# Input array
arr = [7, 1, 5, 3, 6, 4]

# Initialize variables
min_element = arr[0]
max_diff = 0

# Traverse array
for i in range(1, len(arr)):
    if arr[i] < min_element:
        min_element = arr[i]
    else:
        diff = arr[i] - min_element
        if diff > max_diff:
            max_diff = diff

print("Maximum Difference:", max_diff)