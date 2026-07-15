# MaxProduct

n = int(input("Enter the number of elements: "))

print("Enter the array elements:")
arr = list(map(int, input().split()))

max_product = arr[0] * arr[1]
first = arr[0]
second = arr[1]

for i in range(n):
    for j in range(i + 1, n):
        product = arr[i] * arr[j]

        if product > max_product:
            max_product = product
            first = arr[i]
            second = arr[j]

print("Pair with Maximum Product:", first, second)
print("Maximum Product =", max_product)