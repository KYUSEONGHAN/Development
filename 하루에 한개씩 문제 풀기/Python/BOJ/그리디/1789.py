# boj, 1789 : 수들의 합, python3
# 그리디 알고리즘
import sys


def num_sum(target):
    result = 1
    cnt = 2

    while True:
        if result > target:
            return cnt - 2
        result += cnt
        cnt += 1


S = int(sys.stdin.readline())

print(num_sum(S))