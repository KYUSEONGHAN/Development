# https://www.acmicpc.net/problem/11557
# boj, 11557: yangjojang of the year, python3
import sys

input = sys.stdin.readline

def solve(l):
    for x in l:
        print(max(x, key=lambda x: int(x[1]))[0])

if __name__ == '__main__':
    t = int(input())
    yanjojang_l = []

    for _ in range(t):
        n = int(input())
        l = [list(map(str, input().split())) for _ in range(n)]
        yanjojang_l.append(l)

    solve(yanjojang_l)