# My Travel Ticket Counter

# Travel booking details
traveler_name = input("Enter Traveler Name: ")
destination = input("Enter Destination: ")

# Ticket prices
ticket_price1 = float(input("Enter Ticket Price 1: "))
ticket_price2 = float(input("Enter Ticket Price 2: "))

# Calculate total ticket cost
total_cost = ticket_price1 + ticket_price2

# Display booking details
print("\n----- Travel Booking Details -----")
print("Traveler Name:", traveler_name)
print("Destination:", destination)
print("Ticket Price 1:", ticket_price1)
print("Ticket Price 2:", ticket_price2)
print("Total Ticket Cost:", total_cost)

# Compare ticket prices
if ticket_price1 > ticket_price2:
    print("Ticket Price 1 is more expensive than Ticket Price 2.")
elif ticket_price1 < ticket_price2:
    print("Ticket Price 2 is more expensive than Ticket Price 1.")
else:
    print("Both ticket prices are equal.")

# String operations
print("\nWelcome,", traveler_name.upper())
print("Your destination is", destination.title())

# Swap ticket prices
ticket_price1, ticket_price2 = ticket_price2, ticket_price1

print("\nAfter Swapping Ticket Prices:")
print("Ticket Price 1:", ticket_price1)
print("Ticket Price 2:", ticket_price2)