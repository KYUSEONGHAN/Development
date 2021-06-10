# boj, 2581 : 소수, python3
# 수학, 정수론, 소수 판정
import sys


def eratos(s, n):
    sieve = [1] * (n + 1)

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * 2, n + 1, i):
                sieve[j] = 0

    return [i for i in range(2, n + 1) if sieve[i] and i >= s]


def sosu(start, end):
    l = eratos(start, end)

    if len(l) == 0:
        return -1

    return '\n'.join(map(str, [sum(l), l[0]]))


if __name__ == '__main__':
    M = int(sys.stdin.readline())
    N = int(sys.stdin.readline())

    print(sosu(M, N))