# https://www.acmicpc.net/problem/1012
# boj, 1012: 유기농 배추, python3
from sys import setrecursionlimit, stdin

# 재귀 호출로인한 시간 초과를 피하기 위해서
setrecursionlimit(10**7)

input = stdin.readline

# 이동방향 정의
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def dfs(x, y):
    # 현재 위치 방문 처리
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 주어진 범위를 벗어나는지 체크
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 이동한 위치가 배추이며 처음 방문한 경우에만
        if graph[nx][ny] == 1 and visited[nx][ny] == False:
            dfs(nx, ny)


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        m, n, k = map(int, input().split())
        cabbage = [list(map(int, input().split())) for _ in range(k)]
        graph = [[0] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        cnt = 0

        for x, y in cabbage:
            graph[y][x] = 1

        for x in range(n):
            for y in range(m):
                # 현재 위치에 배추가 있고 처음 방문한 경우에만
                if graph[x][y] == 1 and visited[x][y] == False:
                    dfs(x, y)
                    cnt += 1

        print(cnt)
