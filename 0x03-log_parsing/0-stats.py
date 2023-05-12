#!/usr/bin/python3
'''Script -> reads stdin line by line & computes metrics'''


import sys

cache_scode = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
cnt = 0
t_size = 0

try:
    for line_list in map(str.split, sys.stdin):
        if len(line_list) > 4:
            cd = line_list[-2]
            size = int(line_list[-1])
            if cd in cache_scode:
                cache_scode[cd] += 1
            t_size += size
            cnt += 1

        if cnt == 10:
            print(f'File size: {t_size}')
            for key, value in sorted(cache_scode.items()):
                if value != 0:
                    print(f'{key}: {value}')
            cnt = 0

except Exception as err:
    pass

finally:
    print(f'File size: {t_size}')
    for key, value in sorted(cache_scode.items()):
        if value != 0:
            print(f'{key}: {value}')
