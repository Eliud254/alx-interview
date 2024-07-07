#!/usr/bin/python3
"""The module for Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculation of the perimeter of the island
    described in the grid.

    Args:
      the grid (list of list of int): The grid
        representing the island.

    Returns:
        int:  perimeter of the island.
    """
    # Determing the number of rows /the columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initializing the perimeter variable to 0
    perimeter = 0

    # Looping through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Checking if the current cell represents land
            if grid[i][j] == 1:
                # Checking the top edge
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1  # Adding 1 to the perimeter for top edge

                # Checking the bottom edge
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1

                # Check the left edge
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1  # Adding 1 to the perimeter for  left edge

                # Checking the right edge
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1  # Adding 1 to the perimeter

    # Returning the total perimeter
    return perimeter
