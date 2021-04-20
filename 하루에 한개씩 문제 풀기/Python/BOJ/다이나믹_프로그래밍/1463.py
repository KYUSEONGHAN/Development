# boj, 1463 : 1로 만들기, python
# dp : 큰 문제를 작은 문제로 나눠서 푸는 알고리즘
import sys


def DP(N):
    for i in range(2, N + 1):
        d[i] = d[i - 1] + 1

        if all((i % 2 == 0, d[i] > d[i // 2] + 1)):
            d[i] = d[i // 2] + 1
        if all((i % 3 == 0, d[i] > d[i // 3] + 1)):
            d[i] = d[i // 3] + 1

    return d[N]


N = int(sys.stdin.readline())

d = [0] * (N + 1)

print(DP(N))