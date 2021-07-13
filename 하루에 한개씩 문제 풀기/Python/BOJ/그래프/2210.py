# boj, 2210 : 숫자판 점프, python3
# 브루트포스 알고리즘, 그래프 탐색, 깊이 우선 탐색
import sys

def dfs(x, y, number, result):
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k]

        if 0 <= ddx < 5 and 0 <= ddy < 5:
            dfs(ddx, ddy, number + matrix[ddx][ddy], result)


def solve():
    result = []

    for i in range(5):
        for j in range(5):
            dfs(i, j, matrix[i][j], result)

    return len(result)


matrix = [list(map(str, sys.stdin.readline().split())) for _ in range(5)]

print(solve())