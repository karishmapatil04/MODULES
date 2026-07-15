# Matrix Subtraction

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of First Matrix:")
matrix1 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix1.append(row)

print("Enter elements of Second Matrix:")
matrix2 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix2.append(row)

# Subtract the matrices
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] - matrix2[i][j])
    result.append(row)

# Display the result
print("Resultant Matrix after Subtraction:")
for i in range(rows):
    for j in range(cols):
        print(result[i][j], end=" ")
    print()