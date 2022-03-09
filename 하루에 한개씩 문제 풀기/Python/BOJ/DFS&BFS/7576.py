# https://www.acmicpc.net/problem/7576
# boj, 7576: 토마토, python3
from collections import deque
import sys

input = sys.stdin.readline

# 이동방향 정의
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs():
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 상, 하, 좌, 우 위치 체크
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 주어진 범위를 벗어나는지 확인
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 인근 안익은 토마토를 익도록
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx, ny))

def solve():
    # bfs 탐색 수행
    bfs()
    result = 0

    for tomato in graph:
        if 0 in tomato:
            return -1
        max_ = max(tomato)
        result = max(max_, result)

    return result - 1


if __name__ == '__main__':
    m, n = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    # bfs 구현을 위해 queue 구현
    queue = deque()

    for x in range(n):
        for y in range(m):
            # 토마토가 있는 위치여야만 bfs 탐색 수행
            if graph[x][y] == 1:
                queue.append((x, y))

    print(solve())
