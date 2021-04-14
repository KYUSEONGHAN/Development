# boj, 1929 : 소수 구하기, python
import sys


def get_sosu(start, end):
    a = [False, False] + [True] * (end - 1)
    primes = []

    for i in range(2, end + 1):
        if a[i]:
            primes.append(i)
        for j in range(2 * i, end + 1, i):
            a[j] = False

    result = [i for i in primes if i >= start]

    return '\n'.join(map(str, result))


M, N = map(int, sys.stdin.readline().split())

print(get_sosu(M, N))