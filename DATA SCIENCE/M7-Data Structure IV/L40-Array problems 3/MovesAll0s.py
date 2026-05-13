# Program to move the 0's to the end
 
def pushZerosToEnd(a, a_size):
 
    # Zero will hold the position where non zero numbers should be
    zero = 0
 
    # Non zero will iterate to find if the current number is zero or non zero
    nonzero = 0
 
    while(nonzero!=a_size):
        if a[nonzero]!=0:
            a[nonzero],a[zero] = a[zero],a[nonzero]
            zero+=1
        nonzero+=1
        
# Driver code
a = [1,0,3,6,0,0,0,2,355,0,72]
a_size = len(a)
print(a)
pushZerosToEnd(a, a_size)
print("Array after pushing all zeros to end of array:")
print(a)
