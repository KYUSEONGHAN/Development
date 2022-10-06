# https://www.acmicpc.net/problem/15651
# boj, 15651: n과 m (3), python3
from itertools import product
import sys

input = sys.stdin.readline

def solve(n: int, m: int):
    for x in list(product(range(1, n+1), repeat=m)):
        print(*x)

if __name__ == '__main__':
    n, m = map(int, input().split())  # (1 ≤ M ≤ N ≤ 7)

    solve(n, m)