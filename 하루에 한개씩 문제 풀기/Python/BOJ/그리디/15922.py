# boj, 15922 : 아우으 우아으이야!!, python3
# 그리디 알고리즘
import sys


def solve(n, l):
    start = l[0][0]
    end = l[0][1]

    target = end - start

    for i in range(1, n):
        if l[i][0] <= end and l[i][1] <= end:
            continue

        target += l[i][1] - l[i][0]

        if l[i][0] < end:
            target -= (end - l[i][0])

        start = l[i][0]
        end = l[i][1]

    return target


N = int(sys.stdin.readline())
x_y_list = []

for i in range(N):
    x_y = list(map(int, sys.stdin.readline().split()))
    x_y_list.append(x_y)

print(solve(N, sorted(x_y_list)))