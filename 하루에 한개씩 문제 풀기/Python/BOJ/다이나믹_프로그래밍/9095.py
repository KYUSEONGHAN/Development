# boj, 9095 : 1, 2, 3 더하기, python
import sys


def DP(n):
    for _ in range(3, 11):
        d.append(sum(d[-3:]))

    return d[n - 1]


T = int(sys.stdin.readline())
d = [1, 2, 4]

for _ in range(T):
    n = int(sys.stdin.readline())
    print(DP(n))