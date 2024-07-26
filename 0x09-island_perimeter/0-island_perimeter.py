#!/usr/bin/python3
"""
Island Perimeter
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list): List of list of integers representing the grid.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Check for water or edge on all four sides
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1  # Top
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1  # Bottom
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1  # Left
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1  # Right
    return perimeter

