# Add two lists using map and lambda
list1 = [1, 2, 3]
list2 = [4, 5, 6,8]
result = map(lambda x, y: x + y, list1,list2)
print("Addition of two lists")
print(list(result))

#using map
nums = [1, 2, 3, 4, 5]  
def sq(n):    
    return n*n  
square = list(map(sq, nums))
print("Square of numbers in list")
print(square)