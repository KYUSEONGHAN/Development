# boj, 11651 : 좌표 정렬하기2, python3
import sys

N = int(sys.stdin.readline())
point = []

for i in range(N):
    x_y = list(map(int, sys.stdin.readline().split()))
    point.append(x_y)

point.sort(key=lambda x: (x[1], x[0]))

for i in point:
    print(i[0], i[1])