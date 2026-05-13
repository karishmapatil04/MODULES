# Program to find the equilibrium index for an array index, array
 
def equilibriumPoint(arr):
    leftSideSum = 0
    rightSideSum = 0
    n = len(arr)
 
    # Go to each indx of the array and check if it an equilibrium point
    for i in range(n):
        leftSideSum = 0
        rightSideSum = 0
    
        # get left sum
        for j in range(i):
            leftSideSum += arr[j]
        
        # get right sum
        for j in range(i + 1, n):
            rightSideSum += arr[j]
        
        # if leftsum and rightsum are same,
        # then we are done
        if leftSideSum == rightSideSum:
            return i
 
    return -1
 
arr = [-4,6,2,0,0,1,1]
print ("Element  : ",arr[equilibriumPoint(arr)])
