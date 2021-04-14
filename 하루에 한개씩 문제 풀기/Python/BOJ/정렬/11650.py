# boj, 11650 : 좌표 정렬하기, python3
import sys

N = int(sys.stdin.readline())
point = []

for i in range(N):
    x_y = list(map(int, sys.stdin.readline().split()))
    point.append(x_y)

point.sort()

for i in point:
    print(i[0], i[1])