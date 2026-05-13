# Recursive Function 1
def function1(n):
    if n <= 1:
        return
    function1(n - 1)

# Time Complexity: O(n)


# Recursive Function 2
def function2(n):
    if n <= 1:
        return
    function2(n - 1)
    function2(n - 1)

# Time Complexity: O(2^n)


# Driver Code
n = 5

print("Calling Function 1:")
function1(n)

print("Calling Function 2:")
function2(n)