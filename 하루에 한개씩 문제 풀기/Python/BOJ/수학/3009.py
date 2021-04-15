# boj, 3009 : 네 번째 점, python3
import sys

x_list = []
y_list = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

for i in x_list:
    if x_list.count(i) == 1:
        result_x = i
for i in y_list:
    if y_list.count(i) == 1:
        result_y = i

print(result_x, result_y)