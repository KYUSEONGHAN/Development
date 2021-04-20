# boj, 9184 : 신나는 함수 실행, python
# DP algorithm : 큰 문제를 작은 문제로 나눠서 푸는 알고리즘
import sys


def w(a, b, c):
    if any((a <= 0, b <= 0, c <= 0)):
        return 1
    elif any((a > 20, b > 20, c > 20)):
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    if all((a < b, b < c)):
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

    return dp[a][b][c]


dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())

    if all((a == -1, b == -1, c == -1)):
        break
    print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))