def check_value_frequency(test_dict, value):
    """
    Count how many times a value appears in the dictionary.
    
    Parameters:
        test_dict (dict): The dictionary to check
        value: The value whose frequency is to be counted
    
    Returns:
        int: Frequency of the value
    """
    count = 0
    for v in test_dict.values():
        if v == value:
            count += 1
    return count


# Example dictionary
test_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 10
}

# Value to check
value_to_check = 10

frequency = check_value_frequency(test_dict, value_to_check)

print("Dictionary:", test_dict)
print("Value to check:", value_to_check)
print("Frequency of value:", frequency)