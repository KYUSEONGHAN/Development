# boj, 2828 : 사과 담기 게임, python3
# 그리디 알고리즘
import sys


def apple_game(n, m, l):
    basket = m - 1
    left = 1
    right = left + basket
    result = 0

    for x in l:
        if x < left:
            result += left - x
            left, right = x, x + basket
        elif x > right:
            result += x - right
            left, right = x - basket, x

    return result


N, M = map(int, sys.stdin.readline().split())
j = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for i in range(j)]

print(apple_game(N, M, l))