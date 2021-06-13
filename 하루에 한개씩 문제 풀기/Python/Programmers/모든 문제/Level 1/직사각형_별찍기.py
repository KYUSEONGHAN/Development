# programmers, phase1 : 직사각형 별찍기, python3
import sys


def solve(n, m):
    star = [['*' for j in range(n)] for i in range(m)]

    for i in star:
        print(''.join(i))


n, m = map(int, sys.stdin.readline().split())

solve(n, m)
