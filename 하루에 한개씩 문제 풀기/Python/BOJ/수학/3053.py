# boj, 3053 : 택시 기하학, python3
# 수학 알고리즘
import sys
from math import pi


def euclid(r):
    return f'{pi * r * r:.6f}'


def taxi(r):
    return f'{2 * r * r}.000000'


if __name__ == '__main__':
    R = int(sys.stdin.readline())

    print(euclid(R))
    print(taxi(R))