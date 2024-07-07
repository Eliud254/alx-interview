#!/usr/bin/python3
"""
Defines the function island_perimeter
to compute the perimeter
of an island represented in a grid.
"""

bound_4 = set()
bound_3 = set()
bound_2 = set()
bound_1 = set()


def boundary(grid, i, j):
    """
    Determine the number of exposed boundaries
    for a cell and categorize it.

    Args:
        grid (list): 2D list representing the island and water.
        i (int): Row index of the cell.
        j (int): Column index of the cell.
    """
    boundaries = 0
    try:
        if i == 0 or grid[i-1][j] == 0:
            boundaries += 1
    except IndexError:
        boundaries += 1
    try:
        if grid[i+1][j] == 0:
            boundaries += 1
    except IndexError:
        boundaries += 1
    try:
        if grid[i][j+1] == 0:
            boundaries += 1
    except IndexError:
        boundaries += 1
    try:
        if j == 0 or grid[i][j-1] == 0:
            boundaries += 1
    except IndexError:
        boundaries += 1

    if boundaries == 1:
        bound_1.add((i, j))
    elif boundaries == 2:
        bound_2.add((i, j))
    elif boundaries == 3:
        bound_3.add((i, j))
    elif boundaries == 4:
        bound_4.add((i, j))


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list): 2D list of integers (0 for water, 1 for land).

    Returns:
        int: The perimeter of the island.
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                boundary(grid, i, j)
                if bound_4:
                    return 4

    perimeter = (len(bound_3) * 3) + (len(bound_2) * 2) + len(bound_1)
    return perimeter
