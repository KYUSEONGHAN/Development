# https://www.acmicpc.net/problem/7569
# boj, 7569: 토마토, python3
import sys
from collections import deque

input = sys.stdin.readline

# x, y, z 3차원 이동방향 정의
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 인접한 노드를 탐색하여 최소 일수를 반환해야하는 문제이므로 bfs로 접근.
def bfs():
    # 큐가 빌 때까지 반복문 수행
    while queue:
        x, y, z = queue.popleft()
        # 이동방향 체크
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # 주어진 범위를 벗어나는지 체크
            if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
                continue
            # 이동 방향에 익지않은 토마토인 곳만
            if graph[nz][nx][ny] == 0:
                # 익은 토마토 처리
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nx, ny, nz))


def solve():
    # bfs 탐색 수행
    bfs()
    result = 0

    for z in graph:
        for tomato in z:
            # 모든 토마토가 익지 못하는 상황이라면 -1 출력
            if 0 in tomato:
                return -1
            max_ = max(tomato)
            result = max(max_, result)

    return result - 1


if __name__ == '__main__':
    m, n, h = map(int, input().split())
    graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    # bfs 수행을 위한 queue 선언
    queue = deque()

    for z in range(h):
        for x in range(n):
            for y in range(m):
                # 토마토가 있는 위치에서만
                if graph[z][x][y] == 1:
                    # queue에 토마토 위치 입력
                    queue.append((x, y, z))

    print(solve())