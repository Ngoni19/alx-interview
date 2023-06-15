#!/usr/bin/python3
"""
This function takes in a list of coin values and a total amount, and returns the minimum number of coins needed to make up that total. If the total cannot be reached, the program returns -1.

Parameters:
-----------
coins (list): A list of integers representing the values of coins available to make change
total (int): The total amount to make change for

Returns:
--------
int: The minimum number of coins required to make up the total amount, or -1 if it is not possible.
"""

import sys


def makeChange(coins, total):
    '''
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    if total <= 0:
        return 0
    table = [sys.maxsize for j in range(total + 1)]
    table[0] = 0
    m = len(coins)
    for j in range(1, total + 1):
        for j in range(m):
            if coins[j] <= j:
                subres = table[j - coins[j]]
                if subres != sys.maxsize and subres + 1 < table[j]:
                    table[j] = subres + 1

    if table[total] == sys.maxsize:
        return -1
    return table[total]
