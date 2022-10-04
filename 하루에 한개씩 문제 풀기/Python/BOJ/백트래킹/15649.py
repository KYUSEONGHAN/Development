# https://www.acmicpc.net/problem/15649
# boj, 15649: n과 m (1), python3
from itertools import permutations
import sys

input = sys.stdin.readline

def solve(n: int, m: int):
    for x in list(permutations(range(1, n+1), m)):
        print(*x)


if __name__ == '__main__':
    n, m = map(int, input().split())  # (1 ≤ M ≤ N ≤ 8)

    solve(n, m)