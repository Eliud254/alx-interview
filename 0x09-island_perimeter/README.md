Island Perimeter Challenge
This project solves the "Island Perimeter" challenge following the requirements and style guide provided.

Functionality:

Calculates the perimeter of the island in a 2D grid.
The grid represents a map where:
0 represents water.
1 represents land.
How to Use:

Save the code as 0-island_perimeter.py.
Run the script: python3 0-island_perimeter.py
Example Usage:

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

perimeter = island_perimeter(grid)
print(perimeter)  # Output: 12
Technical Details:

Python 3 (version 3.4.3)
PEP 8 Style Guide (version 1.7)
Note:

This solution assumes there is only one island in the grid.
