def longest_ones(n):
    count = 0
    max_count = 0

    while n > 0:
        if n & 1:              # if last bit is 1
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
        n = n >> 1             # shift right

    return max_count


# Input
num = int(input("Enter a number: "))

# Output
print("Longest consecutive 1's:", longest_ones(num))