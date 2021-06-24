# boj, 11508 : 2+1 세일, python3
# 그리디 알고리즘
import sys


def two_plus_one(l):
    result = 0
    chunk = [l[i:i + 3] for i in range(0, len(l), 3)]

    for i in chunk:
        if len(i) != 1:
            result += i[0] + i[1]
        else:
            result += i[0]

    return result


N = int(sys.stdin.readline())

price = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse=True)

print(two_plus_one(price))