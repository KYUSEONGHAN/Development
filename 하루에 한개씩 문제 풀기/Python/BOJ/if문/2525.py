# https://www.acmicpc.net/problem/2525
# boj, 2525: 오븐 시계, python3
import sys

input = sys.stdin.readline

def solve(h, m, cook_time):
    h += cook_time // 60
    m += cook_time % 60

    if m >= 60:
        h += 1
        m -= 60

    if h >= 24:
        h -= 24

    return h, m

if __name__ == '__main__':
    h, m = map(int, input().split())
    cook_time = int(input())
    print(*solve(h, m, cook_time))