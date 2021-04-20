import sys
from collections import OrderedDict

n = int(input())
baduk = [[0 for j in range(1, 20)] for i in range(1, 20)]
x_y = []
cnt = 0

for _ in range(n):
    location = list(map(int, input().split()))
    x_y.append(location)

x_y_tuple = [tuple(x) for x in x_y]
without_overlap = list(OrderedDict.fromkeys(x_y_tuple))

for i in without_overlap:
    baduk[i[0] - 1][i[1] - 1] += 1

for _ in range(20):
    print(" ".join(map(str, baduk[cnt])))
    cnt += 1