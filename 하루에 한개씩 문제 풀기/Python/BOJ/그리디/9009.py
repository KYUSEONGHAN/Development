# boj, 9009 : 피보나치, python3
# 그리디 알고리즘
import sys


def solution(n):
    fibonacci = [0, 1]
    result = []

    for i in range(2, 45):
        fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])

    for i in range(len(fibonacci) - 1, 0, -1):
        if fibonacci[i] <= n:
            n -= fibonacci[i]
            result.append(fibonacci[i])

    result.sort()

    return ' '.join(map(str, result))


T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    print(solution(n))
