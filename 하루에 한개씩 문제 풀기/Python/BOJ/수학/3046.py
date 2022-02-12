# https://www.acmicpc.net/problem/3046
# boj, 3046: R2, python3
import sys

input = sys.stdin.readline

def solve(r1, s):
    # s == (r1 + r2) // 2
    # 2s == (r1 +r2)
    # r2 = 2s - r1
    return 2*s - r1

if __name__ == '__main__':
    r1, s = map(int, input().split())

    print(solve(r1, s))