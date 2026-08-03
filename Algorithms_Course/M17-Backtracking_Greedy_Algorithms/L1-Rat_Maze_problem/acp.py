# Count number of ways to reach destination in a maze using Backtracking

def countWays(maze, x, y, n, visited):
    # If destination is reached
    if x == n - 1 and y == n - 1:
        return 1

    # Boundary and validity check
    if x < 0 or y < 0 or x >= n or y >= n:
        return 0
    if maze[x][y] == 0 or visited[x][y]:
        return 0

    # Mark current cell as visited
    visited[x][y] = True

    # Explore all four directions
    ways = 0
    ways += countWays(maze, x + 1, y, n, visited)  # Down
    ways += countWays(maze, x - 1, y, n, visited)  # Up
    ways += countWays(maze, x, y + 1, n, visited)  # Right
    ways += countWays(maze, x, y - 1, n, visited)  # Left

    # Backtrack
    visited[x][y] = False

    return ways


# Main Program
n = int(input("Enter size of maze (n): "))

print("Enter the maze (1 = Open path, 0 = Blocked path):")
maze = []
for i in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

visited = [[False] * n for _ in range(n)]

if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
    print("Number of ways: 0")
else:
    result = countWays(maze, 0, 0, n, visited)
    print("Number of ways:", result)