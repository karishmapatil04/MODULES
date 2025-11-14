def printPowerSet(input_set):
    set_size = len(input_set)
    power_set_size = 2 ** set_size  # Total number of subsets

    # Loop over all possible subset combinations
    for counter in range(power_set_size):
        subset = []
        for j in range(set_size):
            # Check if j-th bit in counter is set
            if counter & (1 << j):
                subset.append(input_set[j])
        print(subset)

# Example usage
my_set = [1, 2, 3]
printPowerSet(my_set)