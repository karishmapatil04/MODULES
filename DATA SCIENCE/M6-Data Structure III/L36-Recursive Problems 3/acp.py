def maze_path(rows, cols):
    # Base case: reached destination
    if rows == 1 or cols == 1:
        return 1

    # Recursive case
    return maze_path(rows - 1, cols) + maze_path(rows, cols - 1)


# Input maze size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Function call
ways = maze_path(rows, cols)

print("Number of ways the rat can escape the maze:", ways)