#!/usr/bin/python3
'''
A module that contains a function that determines if a given data set
represents a valid UTF-8 encoding.
'''


def validUTF8(data):
    '''
    A function that determines if a given data set is a valid
    UTF-8 encoding.

    Args:
        data (list): A list of integers representing the data to be checked.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    '''
    byte_count = 0

    for i in data:
        if byte_count == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                byte_count = 1
            elif i >> 4 == 0b1110:
                byte_count = 2
            elif i >> 3 == 0b11110:
                byte_count = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            byte_count -= 1
    return byte_count == 0
