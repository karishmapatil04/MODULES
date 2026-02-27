def find_symmetric_difference(set1, set2):
    """
    Returns the symmetric difference between two sets.
    """
    return set1.symmetric_difference(set2)


# Example sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = find_symmetric_difference(set1, set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Symmetric Difference:", result)