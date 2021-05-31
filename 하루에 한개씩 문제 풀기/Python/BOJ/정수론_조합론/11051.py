# boj, 11051 : 이항 계수2, python3
# 정수론 및 조합론
# 다이나믹 프로그래밍
import sys


def choose(cache, times, left):
    if times == 0:
        return left == 0

    if cache[times][left] != -1:
        return cache[times][left]

    cache[times][left] = choose(cache, times - 1, left) + choose(cache, times - 1, left - 1)

    return cache[times][left]


def bino_coef(n, k):
    if k > n:
        return 0

    cache = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    return choose(cache, n, n - k)


N, K = map(int, sys.stdin.readline().split())

print(bino_coef(N, K) % 10007)