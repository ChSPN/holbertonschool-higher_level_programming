#!/usr/bin/python3

"""
module
"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing the Pascal's triangle of n.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        A list of lists of integers representing the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        for j in range(len(last_row) - 1):
            row.append(last_row[j] + last_row[j + 1])
        row.append(1)
        triangle.append(row)

    return triangle
