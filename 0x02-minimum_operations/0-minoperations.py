#!/usr/bin/python3
'''Script for finding The minimum operations coding challenge.
'''


def minOperations(n):
    '''Method: computes the fewest number of operations needed to result
    in exactly (n) H characters.
    '''
    if not isinstance(n, int) or n < 1:
        return 0
    # use memoization to avoid recomputation
    memo = {0: 0, 1: 0}
    for k in range(2, n + 1):
        memo[k] = float('inf')
        for j in range(1, k):
            if k % j == 0:
                memo[k] = min(memo[k], memo[j] + k // j)
    return memo[n]
