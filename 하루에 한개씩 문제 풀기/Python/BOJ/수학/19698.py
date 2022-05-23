# https://www.acmicpc.net/problem/19698
# boj, 19698: 헛간 청약, python3
import sys

input = sys.stdin.readline

def solve(n: int, w: int, h: int, l: int) -> int:
    return (w // l) * (h // l) if (w // l) * (h // l) <= n else n

if __name__ == '__main__':
    n, w, h, l = map(int, input().split())

    print(solve(n, w, h, l))