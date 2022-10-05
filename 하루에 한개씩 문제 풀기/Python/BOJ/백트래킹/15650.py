# https://www.acmicpc.net/problem/15650
# boj, 15650: n과 m (2), python3
from itertools import combinations
import sys

input = sys.stdin.readline

def solve(n: int, m: int):
    for x in list(combinations(range(1, n+1), m)):
        print(*x)

if __name__ == '__main__':
    n, m = map(int, input().split())  # (1 ≤ M ≤ N ≤ 8)

    solve(n, m)