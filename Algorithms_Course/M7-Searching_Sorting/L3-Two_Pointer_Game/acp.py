# IsThereAPairWithNearestSum

n = int(input("Enter the number of elements: "))

print("Enter the sorted array elements:")
arr = list(map(int, input().split()))

target = int(input("Enter the target sum: "))

left = 0
right = n - 1

min_diff = float('inf')
pair = ()

while left < right:
    current_sum = arr[left] + arr[right]
    diff = abs(target - current_sum)

    if diff < min_diff:
        min_diff = diff
        pair = (arr[left], arr[right])

    if current_sum < target:
        left += 1
    elif current_sum > target:
        right -= 1
    else:
        break

print("Pair with Nearest Sum:", pair)
print("Nearest Sum =", pair[0] + pair[1])