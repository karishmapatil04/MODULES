# Rotate Array with Inputs

n = int(input("Enter the number of elements: "))

print("Enter the array elements:")
arr = list(map(int, input().split()))

# Left Rotate by 1
rotate_one = arr[1:] + arr[:1]

# Left Rotate by 2
rotate_two = arr[2:] + arr[:2]

print("Array after Left Rotation by 1:")
for i in rotate_one:
    print(i, end=" ")

print("\nArray after Left Rotation by 2:")
for i in rotate_two:
    print(i, end=" ")