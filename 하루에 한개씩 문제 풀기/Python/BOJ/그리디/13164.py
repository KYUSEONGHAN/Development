# boj, 13164 : 행복 유치원, python3
# 그리디 알고리즘
import sys


def kindergarden(k, l):
    result = sorted([l[i + 1] - l[i] for i in range(len(l) - 1)], reverse=True)

    return sum(result[k - 1:])


N, K = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))

print(kindergarden(K, h))
