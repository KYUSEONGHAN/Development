# https://www.acmicpc.net/problem/7562
# boj, 7562: 나이트의 이동, python3
from collections import deque
import sys

input = sys.stdin.readline

# 이동 방향 정의
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs(start_x, start_y, end_x, end_y):
    # 큐 선언
    queue = deque()
    queue.append([start_x, start_y])
    # 현재 위치 방문처리
    graph[start_x][start_y] = 1

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            print(graph[end_x][end_y]-1)
            return

        # 현재 위치에서 이동 방향 체크
        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]
            # 주어진 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= i or ny >= i:
                continue
            # 해당 위치를 처음 방문하는 경우만 체크
            if graph[nx][ny] == 0:
                # 방문처리
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1


n = int(input())

for _ in range(n):
    i = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    graph = [[0] * i for _ in range(i)]

    bfs(start_x, start_y, end_x, end_y)