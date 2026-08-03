def max_sum_no_consecutive(arr):
    n = len(arr)

    if n == 0:
        return 0
    elif n == 1:
        return max(0, arr[0])

    include = max(0, arr[0])
    exclude = 0

    for i in range(1, n):
        new_include = arr[i] + exclude
        new_exclude = max(include, exclude)

        include, exclude = new_include, new_exclude

    return max(include, exclude)

# Example usage:
arr = [3, 2, 7, 10]
print("Maximum sum with no consecutive elements:", max_sum_no_consecutive(arr))