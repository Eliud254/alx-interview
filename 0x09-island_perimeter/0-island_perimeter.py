#!/usr/bin/python3
"""
Defines the function island_perimeter to compute the perimeter
of an island described in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list): 2D list of integers (0 for water, 1 for land).

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check top boundary
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check bottom boundary
                if i == rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check left boundary
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check right boundary
                if j == cols - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
