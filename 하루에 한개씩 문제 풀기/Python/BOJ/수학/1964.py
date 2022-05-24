# https://www.acmicpc.net/problem/1964
# boj, 1964: 오각형, 오각형, 오각형..., python3
import sys

input = sys.stdin.readline

def solve(n: int) -> int:
    return (sum([(x+1) * 3 + 4 for x in range(n-1)]) + 5) % 45678


if __name__ == '__main__':
    n = int(input())

    print(solve(n))