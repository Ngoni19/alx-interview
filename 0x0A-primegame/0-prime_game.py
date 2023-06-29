#!/usr/bin/python3
'''Script -> Prime Game'''

from math import isqrt

def is_winner(x, nums):
    '''
    Determines the winner of the game.

    Parameters:
    x (int): The number of rounds.
    nums (list): List of numbers for each round.

    Returns:
    str: The name of the winner or None if it's a draw.
    '''
    winner_counter = {'Maria': 0, 'Ben': 0}

    for k in range(x):
        round_winner = is_round_winner(nums[k])
        if round_winner is not None:
            winner_counter[round_winner] += 1

    if winner_counter['Maria'] > winner_counter['Ben']:
        return 'Maria'
    elif winner_counter['Ben'] > winner_counter['Maria']:
        return 'Ben'
    else:
        return None


def is_round_winner(n):
    '''
    Determines the winner of a round.

    Parameters:
    n (int): The number for the round.

    Returns:
    str: The name of the round winner or None if it's a draw.
    '''
    list = [k for k in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for k in range(n):
        # get current player
        currentPlayer = players[k % 2]
        selected_idxs = []
        prime = -1
        for idx, num in enumerate(list):
            # if already picked prime num then
            # find if num is multipl of the prime num
            if prime != -1:
                if num % prime == 0:
                    selected_idxs.append(idx)
            # else check is num is prime then pick it
            else:
                if is_prime(num):
                    selected_idxs.append(idx)
                    prime = num
        # if failed to pick then current player lost
        if prime == -1:
            if currentPlayer == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx in reversed(selected_idxs):
                del list[idx]
    return None


def is_prime(n):
    '''
    Checks if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    '''
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
