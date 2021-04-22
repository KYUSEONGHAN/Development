# boj, 2920 : 음계, PyPy3
import sys


def scale(c_major_list):
    asc = sorted(c_major_list)
    des = sorted(c_major_list, reverse=True)

    if c_major_list == asc:
        return 'ascending'
    return 'descending' if c_major_list == des else 'mixed'


c_major_list = list(map(int, sys.stdin.readline().split(' ')))

print(scale(c_major_list))