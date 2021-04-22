# boj, 2156 : 포도주 시식, python
import sys


def DP(wine):
    if n == 1:
        d[0] = wine[0]
    elif n == 2:
        d[0] = wine[0]
        d[1] = wine[0] + wine[1]
    else:
        d[0] = wine[0]
        d[1] = wine[0] + wine[1]
        d[2] = max(d[1], wine[2] + wine[0], wine[2] + wine[1])

    for i in range(3, n):
        d[i] = max(max(wine[i] + wine[i - 1] + d[i - 3], wine[i] + d[i - 2]), d[i - 1])

    return d[n - 1]


n = int(sys.stdin.readline())
wine = [int(sys.stdin.readline()) for i in range(n)]
d = [0] * n

print(DP(wine))