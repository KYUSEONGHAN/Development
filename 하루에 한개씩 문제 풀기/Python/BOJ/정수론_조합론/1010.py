# boj, 1010 : 다리 놓기, python3
# 정수론 및 조합론
# 다이나믹 프로그래밍
import sys


def factorial(num):
    if num <= 1:
        return num
    return factorial(num - 1) * num


def bridge(n, m):
    if n == 1:
        return m
    if n == m:
        return 1

    return factorial(m) // (factorial(m - n) * factorial(n))


T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(bridge(N, M))
