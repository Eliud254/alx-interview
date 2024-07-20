Python
#!/usr/bin/python3

def island_perimeter(grid):
    """Calculates the perimeter of the island in the given grid.

    Args:
        grid (list): A 2D list of integers representing the grid.
                    0 represents water, 1 represents land.

    Returns:
        int: The perimeter of the island in the grid.
    """

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Add 4 for potential edges of a land cell

                # Check left neighbor (if not within grid or water, add 1 to perimeter)
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1

                # Check right neighbor (if not within grid or water, add 1 to perimeter)
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

                # Check top neighbor (if not within grid or water, add 1 to perimeter)
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1

                # Check bottom neighbor (if not within grid or water, add 1 to perimeter)
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1

    return perimeter
