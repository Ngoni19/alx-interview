#!/usr/bin/python3
'''
A module containing an implementation of Pascal's Triangle function.
'''


def combination(n, r):
    '''Compute the combination of two variables'''
    from functools import reduce

    def factorial(n):
        ''' Compute the combination of two variables.'''
        facto = 1
        for z in range(1, n+1):
            facto *= z
        return facto
    return factorial(n) // (factorial(n - r) * factorial(r))


def pascal_triangle(n):
    """
    Generates the Pascal's Triangle for a given power n, excluding (z+y)^n.
    """
    assert type(n) == int
    if n <= 0:
        return []

    triangle = [[1]] + [
        [combination(z, y) for y in range(z+1)]
        for z in range(1, n)
    ]
    return triangle
