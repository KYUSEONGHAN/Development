import sys

background = [[0 for cols in range(10)] for widths in range(10)]

for i in range(10):
    num = sys.stdin.readline().split()
    background[i] = list(map(int, num))

startPoint = (1, 1)

point = [0, 0]
point[0] = startPoint[0]
point[1] = startPoint[1]

status = 0

while status != 2:
    if background[point[0]][point[1]] == 2:
        status = 2
        background[point[0]][point[1]] = 9
    else:
        background[point[0]][point[1]] = 9

        if background[point[0]][point[1] + 1] != 1:
            point[1] = point[1] + 1
        else:
            point[0] = point[0] + 1

        if point[0] > 8:
            point[0] = 8
            break
        if point[1] > 8:
            point = 8
            break

for i in range(10):
    for j in range(10):
        print(background[i][j], end=' ')
    print()