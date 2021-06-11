# boj, 1002 : 터렛, python3
# 수학 알고리즘
from math import sqrt
import sys


def turret(x1, y1, r1, x2, y2, r2):
    distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if distance == 0 and r1 == r2:
        return -1
    elif abs(r1 - r2) == distance or r1 + r2 == distance:
        return 1
    elif abs(r1 - r2) < distance < r1 + r2:
        return 2
    return 0


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
        print(turret(x1, y1, r1, x2, y2, r2))