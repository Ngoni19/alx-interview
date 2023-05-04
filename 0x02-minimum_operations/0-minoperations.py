#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    if not isinstance(n, int) or n < 1:
        return 0
    memo = {0: 0, 1: 0}
    for i in range(2, n + 1):
        memo[i] = float('inf')
        for j in range(1, i):
            if i % j == 0:
                memo[i] = min(memo[i], memo[j] + i // j)
    return memo[n]
