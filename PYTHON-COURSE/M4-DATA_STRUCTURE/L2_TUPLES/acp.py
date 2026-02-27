def multiply_tuple(numbers):
    """
    Calculate the product of all numbers in a tuple.
    
    Parameters:
        numbers (tuple): A tuple containing numeric values
    
    Returns:
        int/float: Product of all elements
    """
    product = 1
    for num in numbers:
        product *= num
    return product


# Example tuple
numbers = (2, 3, 4, 5)

result = multiply_tuple(numbers)

print("Tuple:", numbers)
print("Product of all numbers:", result)