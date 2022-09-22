# https://www.acmicpc.net/problem/25591
# boj, 25591: 푸앙이와 종윤이, Python3
import sys

input = sys.stdin.readline

def solve1(num1: int, num2: int):
    a, b = 100 - num1, 100 - num2
    c = 100 - (a + b)
    d = a * b
    q, r = d // 100, d % 100

    print(a, b, c, d, q, r)
    print(c + q, r)


if __name__ == '__main__':
    num1, num2 = map(int, input().split())

    solve1(num1, num2)