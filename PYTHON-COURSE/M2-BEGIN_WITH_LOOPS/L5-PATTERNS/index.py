# a pattern needs two things:
# 1) how many rows
# 2) how many characters per row
rows=int(input("Enter number of rows"))
for i in range(rows):
    for j in range(i + 1):
        print("*", end="")
    print()