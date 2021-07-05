# boj, 13904 : 과제, python3
# 그리디 알고리즘
import sys


def homework(n, l):
    answer = [0 for _ in range(1000)]

    for i in range(n):
        for j in range(l[i][0] - 1, -1, -1):
            if answer[j] == 0:
                answer[j] = l[i][1]
                break

    return sum(answer)


N = int(sys.stdin.readline())
l = []

for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())
    l.append([d, w])

print(homework(N, sorted(l, reverse=True, key=lambda x: x[1])))