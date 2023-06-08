#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    '''Rotates a 2D matrix 90 degrees clockwise.

    Args:
        matrix (list[list]): A 2D matrix represented as a list of lists.

    Returns:
        None
    '''
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            # Save top left value
            top_left = matrix[left][left + i]
            
            # Move bottom left to top left
            matrix[left][left + i] = matrix[right - i][left]
            
            # Move bottom right to bottom left
            matrix[right - i][left] = matrix[right][right - i]
            
            # Move top right to bottom right
            matrix[right][right - i] = matrix[left + i][right]
            
            # Move top left to top right
            matrix[left + i][right] = top_left
        
        # Shrink the matrix by one layer
        right -= 1
        left += 1

