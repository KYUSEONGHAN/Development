# https://www.acmicpc.net/problem/1247
# boj, 1247: 부호, Python3
import sys

input = sys.stdin.readline

def solve():
    for _ in range(3):
        n = int(input())
        s = sum([int(input()) for _ in range(n)])
        if s == 0:
            print(0)
        elif s > 0:
            print('+')
        elif s < 0:
            print('-')

if __name__ == '__main__':
    solve()