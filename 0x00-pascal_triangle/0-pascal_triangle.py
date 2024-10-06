#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal's triangle of n"""
    if n <= 0:
        return []
    pascal_triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pascal_triangle[i - 1][j - 1] +
                       pascal_triangle[i - 1][j])
        row.append(1)
        pascal_triangle.append(row)
    return pascal_triangle
