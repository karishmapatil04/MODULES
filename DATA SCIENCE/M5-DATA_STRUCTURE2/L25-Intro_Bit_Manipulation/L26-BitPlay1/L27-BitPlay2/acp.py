# Function to implement circuit logic
def circuit(A, B, C):
    # Example circuit:
    # (A AND B) OR (NOT C)
    result = (A and B) or (not C)
    return result


# Input (0 or 1)
A = int(input("Enter A (0/1): "))
B = int(input("Enter B (0/1): "))
C = int(input("Enter C (0/1): "))

# Convert to boolean
A = bool(A)
B = bool(B)
C = bool(C)

# Output
output = circuit(A, B, C)
print("Output of circuit:", int(output))