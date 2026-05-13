# Input array
arr = [1, 1, 0, 0, 0, 1]

# Count groups
count0 = 0
count1 = 0

# First element group
if arr[0] == 0:
    count0 += 1
else:
    count1 += 1

# Traverse array
for i in range(1, len(arr)):
    if arr[i] != arr[i - 1]:
        if arr[i] == 0:
            count0 += 1
        else:
            count1 += 1

# Minimum flips
result = min(count0, count1)

print("Minimum Flips Required:", result)