#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise

    Args:
        matrix (list of list of int): The 2D matrix to rotate.
        Assumes a square matrix.

    Returns:
        None: The rotation is performed in-place.

    Algorithm:
    1. Swap elements of each row and column.
    2. Reverse each row.
    """
    m = len(matrix)

    # Swap elements of each row and column
    for i in range(m):
        for j in range(i, m):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # Reverse each row
    for i in range(m):
        matrix[i] = matrix[i][::-1]
