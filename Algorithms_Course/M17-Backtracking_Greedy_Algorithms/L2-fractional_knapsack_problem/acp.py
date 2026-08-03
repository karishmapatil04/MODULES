# Possibility of moving out of maze using Backtracking

def solveMaze(maze, x, y, n, visited):
    # Destination reached
    if x == n - 1 and y == n - 1:
        return True

    # Check if current cell is valid
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if maze[x][y] == 0 or visited[x][y]:
        return False

    # Mark current cell as visited
    visited[x][y] = True

    # Move in all four directions
    if (solveMaze(maze, x + 1, y, n, visited) or
        solveMaze(maze, x - 1, y, n, visited) or
        solveMaze(maze, x, y + 1, n, visited) or
        solveMaze(maze, x, y - 1, n, visited)):
        return True

    # Backtrack
    visited[x][y] = False
    return False


# Main Program
n = int(input("Enter size of maze: "))

print("Enter the maze (1 = Open path, 0 = Blocked path):")
maze = []
for i in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

visited = [[False] * n for _ in range(n)]

if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
    print("No, it is not possible to move out of the maze.")
else:
    if solveMaze(maze, 0, 0, n, visited):
        print("Yes, it is possible to move out of the maze.")
    else:
        print("No, it is not possible to move out of the maze.")