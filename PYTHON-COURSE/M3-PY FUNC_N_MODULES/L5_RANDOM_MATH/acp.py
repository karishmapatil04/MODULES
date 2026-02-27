import math

def calculate_trig_values(angle_degrees):
    """
    Calculate sin, cos, and tan of an angle in degrees.
    
    Parameters:
        angle_degrees (float): Angle in degrees
    
    Returns:
        tuple: (sin, cos, tan) values
    """
    # Convert degrees to radians
    angle_radians = math.radians(angle_degrees)
    
    sin_value = math.sin(angle_radians)
    cos_value = math.cos(angle_radians)
    tan_value = math.tan(angle_radians)
    
    return sin_value, cos_value, tan_value


# Example usage
angle = float(input("Enter angle in degrees: "))

sin_val, cos_val, tan_val = calculate_trig_values(angle)

print("sin(", angle, ") =", sin_val)
print("cos(", angle, ") =", cos_val)
print("tan(", angle, ") =", tan_val)