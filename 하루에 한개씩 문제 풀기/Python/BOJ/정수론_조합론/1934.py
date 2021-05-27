# boj, 1934 : 최소공배수, python3
# 정수론 및 조합론
import sys


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def solution(num):
    result = []

    for _ in range(num):
        A, B = map(int, sys.stdin.readline().split())
        result.append(lcm(A, B))

    return '\n'.join(map(str, result))


T = int(sys.stdin.readline())

print(solution(T))