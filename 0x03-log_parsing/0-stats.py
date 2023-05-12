#!/usr/bin/python3
'''Script -> reads stdin line by line & computes metrics'''


import sys

cache_scode = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}
cnt = 0
t_size = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache_scode.keys():
                cache_scode[code] += 1
            t_size += size
            cnt += 1

        if cnt == 10:
            cnt = 0
            print('File size: {}'.format(t_size))
            for k, value in sorted(cache_scode.items()):
                if value != 0:
                    print('{}: {}'.format(k, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(t_size))
    for k, value in sorted(cache_scode.items()):
        if value != 0:
            print('{}: {}'.format(k, value))
