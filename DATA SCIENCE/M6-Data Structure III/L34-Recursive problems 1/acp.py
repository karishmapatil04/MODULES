def power_of_2(n):
    # Base case
    if n == 0:
        return 1
    
    # Recursive case
    return 2 * power_of_2(n - 1)


# Input from user
num = int(input("Enter the power: "))

# Function call
result = power_of_2(num)

# Display result
print("2 raised to the power", num, "is:", result)