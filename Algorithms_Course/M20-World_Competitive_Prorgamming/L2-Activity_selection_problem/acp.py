# Closest Pair of Points - O(n log n)

import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def bruteForce(points):
    minDist = float('inf')
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            minDist = min(minDist, distance(points[i], points[j]))

    return minDist

def stripClosest(strip, d):
    minDist = d
    strip.sort(key=lambda point: point[1])

    n = len(strip)
    for i in range(n):
        j = i + 1
        while j < n and (strip[j][1] - strip[i][1]) < minDist:
            minDist = min(minDist, distance(strip[i], strip[j]))
            j += 1

    return minDist

def closestUtil(points):
    n = len(points)

    if n <= 3:
        return bruteForce(points)

    mid = n // 2
    midPoint = points[mid]

    dl = closestUtil(points[:mid])
    dr = closestUtil(points[mid:])

    d = min(dl, dr)

    strip = []
    for point in points:
        if abs(point[0] - midPoint[0]) < d:
            strip.append(point)

    return min(d, stripClosest(strip, d))

def closest(points):
    points.sort(key=lambda point: point[0])
    return closestUtil(points)

# Main Program
n = int(input("Enter number of points: "))

points = []
print("Enter x and y coordinates:")
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

result = closest(points)

print("Minimum distance =", round(result, 4))