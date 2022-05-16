# https://www.acmicpc.net/problem/15680
# boj, 15680: 연세대학교, python3
import sys

input = sys.stdin.readline

def solve(n: int) -> str:
    return 'YONSEI' if n == 0 else 'Leading the Way to the Future'

if __name__ == '__main__':
    n = int(input())

    print(solve(n))