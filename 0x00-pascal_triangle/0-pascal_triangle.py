#!usr/bin/env python3
"""
finding pascal's triangle
"""


def pascal_triangle(n):
    """
    This function finds pascal's triangle
    """

    pascal_triangle = list()

    if n <= 0:
        return pascal_triangle

    if n > 0:
        pascal_triangle.append([1])

    if n > 1:
        pascal_triangle.append([1, 1])

    for i in range(3, n + 1):
        pascal_triangle.append([0] * i)

        pascal_triangle[i - 1][0] = 1
        pascal_triangle[i - 1][i - 1] = 1
        for j in range(1, i - 1):
            pascal_triangle[i - 1][j] = \
                    pascal_triangle[i - 2][j - 1]\
                    + pascal_triangle[i - 2][j]

        return pascal_triangle
