# https://www.acmicpc.net/problem/9656
# boj, 9656: 돌 게임 2, python3
import sys

input = sys.stdin.readline

def solve(n):
    return 'SK' if n % 2 == 0 else 'CY'

if __name__ == '__main__':
    n = int(input())

    print(solve(n))