# Number of Islands using DFS

def dfs(grid, row, col, rows, cols):
    # Check boundaries and water/visited cells
    if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
        return

    # Mark the current cell as visited
    grid[row][col] = 0

    # Visit all four directions
    dfs(grid, row - 1, col, rows, cols)  # Up
    dfs(grid, row + 1, col, rows, cols)  # Down
    dfs(grid, row, col - 1, rows, cols)  # Left
    dfs(grid, row, col + 1, rows, cols)  # Right


def count_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                islands += 1
                dfs(grid, i, j, rows, cols)

    return islands


# Example grid (1 = Land, 0 = Water)
grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1]
]

print("Number of Islands:", count_islands(grid))