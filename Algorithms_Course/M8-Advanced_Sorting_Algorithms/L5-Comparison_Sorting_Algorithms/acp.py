# Intersection of Sorted Arrays

n1 = int(input("Enter the size of first array: "))
print("Enter the elements of first sorted array:")
arr1 = list(map(int, input().split()))

n2 = int(input("Enter the size of second array: "))
print("Enter the elements of second sorted array:")
arr2 = list(map(int, input().split()))

i = 0
j = 0

print("Intersection of the two arrays:")

while i < n1 and j < n2:
    if arr1[i] == arr2[j]:
        print(arr1[i], end=" ")
        i += 1
        j += 1
    elif arr1[i] < arr2[j]:
        i += 1
    else:
        j += 1