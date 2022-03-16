# https://www.acmicpc.net/problem/2446
# boj, 2446: 별 찍기 -9, python3
import sys

input = sys.stdin.readline

def solve(n):
    star = 2 * n

    for i in range(n):
        print(' ' * i + '*' * (star - (2*i) - 1))

    for i in range(n-2, -1, -1):
        print(' ' * i + '*' * (star - (2*i) - 1))


if __name__ == '__main__':
    n = int(input())

    solve(n)