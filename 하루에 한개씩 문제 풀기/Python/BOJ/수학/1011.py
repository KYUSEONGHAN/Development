# boj, 1011 : fly me to the alpha centauri, python3
# 수학 알고리즘
import sys
import math


def alpha_centauri(start, end):
    interval = end - start
    n = math.sqrt(interval)
    result = int(n) * 2

    if n == int(n):
        result -= 1
    elif interval >= (math.pow(int(n), 2) + math.pow(int(n) + 1, 2)) / 2:
        result += 1

    return result


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for i in range(T):
        x, y = map(int, sys.stdin.readline().split())
        print(alpha_centauri(x, y))