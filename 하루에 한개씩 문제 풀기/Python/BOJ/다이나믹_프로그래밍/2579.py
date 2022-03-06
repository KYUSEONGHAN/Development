# https://www.acmicpc.net/problem/2579
# boj, 2579: 계단 오르기, python3
import sys

input = sys.stdin.readline

def dp(n, staris):
    if n <= 2:
        return sum(stairs)
    # dp table 초기화
    d = [0] * 301
    d[0] = stairs[0]
    d[1] = stairs[0] + stairs[1]

    d[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, n):
        d[i] = max(d[i-3] + stairs[i-1] + stairs[i], d[i-2] + stairs[i])

    return d[n-1]

if __name__ == '__main__':
    n = int(input())
    stairs = [int(input()) for _ in range(n)]

    print(dp(n, stairs))