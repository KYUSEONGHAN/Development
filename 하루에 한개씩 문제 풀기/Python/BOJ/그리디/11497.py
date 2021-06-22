# boj, 11497 : 통나무 건너뛰기, python3
# 그리디 알고리즘
import sys


def tongnamu(l):
    result = 0

    for i in range(len(l) - 2):
        if l[i + 2] - l[i] > result:
            result = l[i + 2] - l[i]

    return result


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(input())
    L = list(map(int, sys.stdin.readline().split()))
    print(tongnamu(sorted(L)))