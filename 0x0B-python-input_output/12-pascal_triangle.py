#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    triangle = []
    row = []
    p_row = []
    for i in range(0, n + 1):
        row = [j > 0 and j < i - 1 and i > 2 and p_row[j-1] + p_row[j] or 1 for j in range(0, i)]
        p_row = row
        triangle += [row]
    return triangle[1:]
