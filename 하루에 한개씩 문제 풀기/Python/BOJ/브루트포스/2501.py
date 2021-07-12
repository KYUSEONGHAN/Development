# boj, 2501 : 약수 구하기, python3
# 브루트포스 알고리즘
import sys


def solve(n, k):
    l = [i for i in range(1, (n // 2) + 1) if n % i == 0] + [n]

    try:
        return l[k - 1]
    except IndexError:
        return 0


N, K = map(int, sys.stdin.readline().split())

print(solve(N, K))