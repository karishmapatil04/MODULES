#Take input
print("Half Pyramid Pattern of Stars (*):")
n = int(input("enter the number of rows: "))
#outer loop to handle number of rows
for row in range(n): 
  #inner loop to handle number of columns
    for j in range(row+1):
      #display result
        print("* ", end="")
    print()