#!/usr/bin/python3
'''Script -> N Queens Challenge'''

import sys


def is_valid(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def is_safe(placed_queens, row, col):
    for r, c in placed_queens:
        if col == c or row - col == r - c or row + col == r + c:
            return False
    return True


def solve_n_queens(n):
    if n < 4:
        return []

    solutions = []
    placed_queens = []

    def backtrack(row):
        if row == n:
            solutions.append(placed_queens[:])
            return
        for col in range(n):
            if is_safe(placed_queens, row, col):
                placed_queens.append((row, col))
                backtrack(row + 1)
                placed_queens.pop()

    backtrack(0)
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2 or not is_valid(sys.argv[1]):
        print("Usage: nqueens N")
        sys.exit(1)

    n = int(sys.argv[1])
    
    try:
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)
    except ValueError:
        print('N must be a number')
        exit(1)

    solutions = solve_n_queens(n)

    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)
