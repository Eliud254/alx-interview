#!/usr/bin/python3
'''The module working with a Pascal's triangle.
'''


def pascal_triangle(n):
    '''Create a list of lists of integers representing
     Pascal's triangle of a given integer.
    '''
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
