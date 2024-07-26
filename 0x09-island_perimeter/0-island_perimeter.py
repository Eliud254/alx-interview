#!/usr/bin/python3
"""Calculate the perimeter of an island in a grid."""


def island_perimeter(grid):
<<<<<<< HEAD
    """Calculate the perimeter of the island in the given grid.
=======
    """
    Calculate the perimeter of the island in a grid.
>>>>>>> 0b68ed9ba3d24b5ad6a1cfe7ec6c9025de266fcf

    Args:
        grid: 2D list of integers (0: water, 1: land)

    Returns:
        Perimeter of the island
    """
    p = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i <= 0 or grid[i - 1][j] == 0:
                    p += 1
                if i >= len(grid) - 1 or grid[i + 1][j] == 0:
                    p += 1
                if j <= 0 or grid[i][j - 1] == 0:
                    p += 1
                if j >= len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    p += 1
    return p
