#!/usr/bin/python3
'''Scipt-> Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''
import sys


def makeChange(coins, total):
    if total <= 0:
        return 0
    table = [sys.maxsize for _ in range(total + 1)]
    table[0] = 0
    
    for k in range(1, total + 1):
        for i, coin in enumerate(coins):
            if coin <= k:
                subres = table[k - coin]
                if subres != sys.maxsize and subres + 1 < table[k]:
                    table[k] = subres + 1
            else:
                break
    
    return table[total] if table[total] < sys.maxsize else -1

