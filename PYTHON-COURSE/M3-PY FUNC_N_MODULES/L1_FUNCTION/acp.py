import math

def calculate_circumference(radius):
    """
    Calculate the circumference of a circle given its radius.
    
    Parameters:
        radius (float): The radius of the circle
    
    Returns:
        float: The circumference of the circle
    """
    return 2 * math.pi * radius


# Example usage
r = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(r)
print("Circumference of the circle:", circumference)