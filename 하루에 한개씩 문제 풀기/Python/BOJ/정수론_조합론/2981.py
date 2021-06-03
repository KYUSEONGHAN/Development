# boj, 2981 : 검문, python3
# 정수론 및 조합론
import sys


def gcd(x, y):
    while y != 0:
        x, y = y, x % y

    return x


def solve(n, l):
    for i in range(n - 1):
        l[i] = abs(l[i + 1] - l[i])
    l.pop()

    number = l[0]

    for i in l:
        number = gcd(number, i)

    answer = set([number])

    for i in range(2, 1 + int(number ** (1 / 2))):
        if number % i == 0:
            answer.add(i)
            answer.add(number // i)

    return ' '.join(map(str, sorted(answer)))


N = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(N)]

print(solve(N, l))