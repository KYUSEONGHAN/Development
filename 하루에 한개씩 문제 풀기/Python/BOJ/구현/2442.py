# boj, 2442: 별 찍기 -5, python3
import sys

input = sys.stdin.readline

def solve(n):
    cnt = 1

    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * cnt)
        cnt += 2


if __name__ == '__main__':
    n = int(input())

    solve(n)