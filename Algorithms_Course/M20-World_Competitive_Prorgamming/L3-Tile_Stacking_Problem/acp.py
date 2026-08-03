# Check if four given points form a square

def distSq(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def isSquare(points):
    distances = []

    # Calculate all 6 pairwise distances
    for i in range(4):
        for j in range(i + 1, 4):
            distances.append(distSq(points[i], points[j]))

    distances.sort()

    # Check square properties
    if (distances[0] > 0 and
        distances[0] == distances[1] == distances[2] == distances[3] and
        distances[4] == distances[5]):
        return True

    return False


# Main Program
points = []

print("Enter the coordinates of 4 points (x y):")
for i in range(4):
    x, y = map(int, input(f"Point {i+1}: ").split())
    points.append((x, y))

if isSquare(points):
    print("The given points form a square.")
else:
    print("The given points do not form a square.")