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
                # Check for land neighbors and subtract shared edges from perimeter
                perimeter += 4  # Potential perimeter for a land cell

                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Subtract left edge if shared with another land cell

                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 2  # Subtract right edge if shared with another land cell

                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract top edge if shared with another land cell

                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 2  # Subtract bottom edge if shared with another land cell

    return perimeter

