# Rotate My Scores

# 1. Reverse using Two Pointers
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    print("Reversed Array:", arr)


# 2. Reverse in Groups
def reverse_groups(arr, k):
    n = len(arr)

    for i in range(0, n, k):
        left = i
        right = min(i + k - 1, n - 1)

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    print("Group Reversed Array:", arr)


# 3. Left Rotate by 1
def left_rotate_one(arr):
    first = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    arr[-1] = first
    print("Left Rotated by 1:", arr)


# 4. Left Rotate by n
def left_rotate_n(arr, d):
    d = d % len(arr)
    arr = arr[d:] + arr[:d]
    print("Left Rotated by", d, ":", arr)


# 5. Find Leaders
def find_leaders(arr):
    leaders = []
    max_right = arr[-1]
    leaders.append(max_right)

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= max_right:
            max_right = arr[i]
            leaders.append(max_right)

    leaders.reverse()
    print("Leaders:", leaders)


# Main Program
scores = list(map(int, input("Enter scores separated by spaces: ").split()))

while True:
    print("\n===== Rotate My Scores =====")
    print("1. Reverse Array")
    print("2. Reverse in Groups")
    print("3. Left Rotate by 1")
    print("4. Left Rotate by n")
    print("5. Find Leaders")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        reverse_array(scores.copy())

    elif choice == 2:
        k = int(input("Enter group size: "))
        reverse_groups(scores.copy(), k)

    elif choice == 3:
        left_rotate_one(scores.copy())

    elif choice == 4:
        d = int(input("Enter rotation value: "))
        left_rotate_n(scores.copy(), d)

    elif choice == 5:
        find_leaders(scores)

    elif choice == 6:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")