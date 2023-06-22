#!/usr/bin/python3
'''Script-> Island Perimeter'''


def island_perimeter(grid):
    '''Method-> returns the perimeter of the island described in grid'''
    cnt = 0
    max_grid = len(grid) - 1  # index of the last list in the grid
    lst_max = len(grid[0]) - 1  # index of the last square in list

    for lst_idx, lst in enumerate(grid):
        for _idx, land in enumerate(lst):
            if land == 1:
                # left and right
                if _idx == 0:
                    # left side
                    cnt += 1

                    # right side
                    if lst[_idx + 1] == 0:
                        cnt += 1
                elif _idx == lst_max:
                    # left side
                    if lst[_idx - 1] == 0:
                        cnt += 1

                    # right side
                    cnt += 1
                else:
                    # left side
                    if lst[_idx - 1] == 0:
                        cnt += 1

                    # right side
                    if lst[_idx + 1] == 0:
                        cnt += 1

                # top and down
                if lst_idx == 0:
                    # top side
                    cnt += 1

                    # bottom side
                    if grid[lst_idx + 1][_idx] == 0:
                        cnt += 1
                elif lst_idx == max_grid:
                    # top side
                    if grid[lst_idx - 1][_idx] == 0:
                        cnt += 1

                    # bottom side
                    cnt += 1
                else:
                    # top side
                    if grid[lst_idx - 1][_idx] == 0:
                        cnt += 1

                    # bottom side
                    if grid[lst_idx + 1][_idx] == 0:
                        cnt += 1

    return cnt
