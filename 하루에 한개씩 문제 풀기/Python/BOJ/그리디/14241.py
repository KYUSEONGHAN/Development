# boj, 14241 : 슬라임 합치기, python3
# 그리디 알고리즘
import sys


def merge_slime(n, l):
    result = 0

    for i in range(n):
        for j in range(i + 1, n):
            result += l[i] * l[j]

    return result


N = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))

print(merge_slime(N, h))