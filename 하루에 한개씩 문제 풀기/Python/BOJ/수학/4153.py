# boj, 4153 : 직각삼각형, Python3
import sys
import math

while True:
    length = sorted(list(map(int, sys.stdin.readline().split())))

    if sum(length) is 0:
        break
    else:
        if int(math.sqrt(length[0] ** 2 + length[1] ** 2)) is length[2]:
            print("right")
            length.clear()
        else:
            print("wrong")
            length.clear()