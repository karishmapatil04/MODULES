# Minimum Number of Platforms Required - Naive Approach

n = int(input("Enter number of trains/buses: "))

arrival = []
departure = []

print("Enter arrival times (in 24-hour format, e.g., 900, 1130):")
for i in range(n):
    arrival.append(int(input()))

print("Enter departure times:")
for i in range(n):
    departure.append(int(input()))

platforms = 1

for i in range(n):
    count = 1
    for j in range(n):
        if i != j:
            # Check if train j overlaps with train i
            if arrival[i] >= arrival[j] and arrival[i] <= departure[j]:
                count += 1
    platforms = max(platforms, count)

print("Minimum number of platforms required =", platforms)