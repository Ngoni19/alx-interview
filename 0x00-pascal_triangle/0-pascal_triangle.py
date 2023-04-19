#!/usr/bin/python3
"""
A module containing an implementation of Pascal's Triangle function.
"""

from functools import reduce


def combination(n, r):
    """
    Compute the combination of two variables.
    """
    def factorial(n):
        """
        Find the factorial of an int
        """
        fac = 1
        for x in range(1, n+1):
            fac *= x
        return fac
    return factorial(n) // (factorial(n - r) * factorial(r))


def pascal_triangle(n):
    """
    Generates the Pascal's Triangle for a given power n, excluding (x+y)^n.
    """
    assert type(n) == int, "n must be an integer!"
    if n <= 0:
        return []

    triangle = [[1]] + [
        [combination(x, y) for y in range(x+1)]
        for x in range(1, n)
    ]
    return triangle
