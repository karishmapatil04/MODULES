# 1 Iteration (O(1))
def multiply_one_iteration(M, N):
    return M * N


# N Iterations (O(N))
def multiply_n_iterations(M, N):
    result = 0
    for i in range(N):
        result += M
    return result


# Input
M = int(input("Enter M: "))
N = int(input("Enter N: "))

# Output
print("1 Iteration Result:", multiply_one_iteration(M, N))
print("N Iteration Result:", multiply_n_iterations(M, N))