# My Smart Switch Bit Monitor

# Input
switches = int(input("Enter the smart switch value (0-255): "))

print("\n===== My Smart Switch Bit Monitor =====")
print("Decimal Value :", switches)
print("Binary Value  :", format(switches, '08b'))

# Count ON switches
on_count = bin(switches).count("1")
print("\nTotal ON Switches:", on_count)

# Check each switch using bit masks
print("\nSwitch Status:")
for i in range(8):
    mask = 1 << i
    if switches & mask:
        print(f"Switch {i}: ON")
    else:
        print(f"Switch {i}: OFF")

# Example: Turn ON switch 2
new_value = switches | (1 << 2)
print("\nAfter Turning ON Switch 2:")
print("Binary Value :", format(new_value, '08b'))

# Example: Turn OFF switch 2
new_value = new_value & ~(1 << 2)
print("\nAfter Turning OFF Switch 2:")
print("Binary Value :", format(new_value, '08b'))

# Example: Toggle switch 0
new_value = switches ^ (1 << 0)
print("\nAfter Toggling Switch 0:")
print("Binary Value :", format(new_value, '08b'))

print("\n===== Monitoring Complete =====")