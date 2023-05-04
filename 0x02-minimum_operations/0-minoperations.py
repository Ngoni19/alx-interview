#!/usr/bin/python3
'''Script for finding The minimum operations coding challenge.
'''


def minOperations(n):
    '''Method: computes the fewest number of operations needed to result
    in exactly (n) H characters.
    '''
    if n < 1:
        return 0
    # use memoization to avoid recomputation    
    memo = [0, 0] + [float('inf')] * (n - 1)
    for k in range(2, n + 1):
        for j in range(2, k + 1):
            if k % j == 0:
                memo[k] = min(memo[k], memo[j] + (k // j))
                break
    return memo[n] if memo[n] != float('inf') else 0
