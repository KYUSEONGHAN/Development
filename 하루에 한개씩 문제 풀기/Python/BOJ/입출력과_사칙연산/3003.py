# https://www.acmicpc.net/problem/3003
# boj, 3003: 킹, 퀸, 룩, 비숍, 나이트, 폰, python3
import sys

input = sys.stdin.readline

def solve(chess: list) -> list:
    answer = [1, 1, 2, 2, 2, 8]

    return [answer[x] - chess[x] for x in range(6)]

if __name__ == '__main__':
    chess = list(map(int, input().split()))

    print(*solve(chess))