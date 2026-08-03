# Minimum Number of Platforms Required (Naive Approach)

n = int(input("Enter number of trains/buses: "))

arrival = []
departure = []

print("Enter arrival times:")
for i in range(n):
    arrival.append(int(input()))

print("Enter departure times:")
for i in range(n):
    departure.append(int(input()))

result = 1

# Compare every train with every other train
for i in range(n):
    platforms = 1

    for j in range(n):
        if i != j:
            # If train j is at the station when train i arrives
            if arrival[i] >= arrival[j] and arrival[i] <= departure[j]:
                platforms += 1

    result = max(result, platforms)

print("Minimum number of platforms required:", result)