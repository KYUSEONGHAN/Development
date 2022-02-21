# https://www.acmicpc.net/problem/11048
# boj, 11048: 이동하기, python3
import sys

input = sys.stdin.readline

def dp(n, m, graph):
    # dp table 초기화
    d = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # dp bottom-up
    for x in range(1, n+1):
        for y in range(1, m+1):
            d[x][y] = max(d[x-1][y], d[x][y-1], d[x-1][y-1]) + graph[x-1][y-1]

    return d[-1][-1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    print(dp(n, m, graph))