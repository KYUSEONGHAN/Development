# https://www.acmicpc.net/problem/2468
# boj, 2468: 안전 영역, Python3
from collections import deque
import sys

input = sys.stdin.readline

# 이동방향 정의
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 탐색 함수
def bfs(x: int, y: int, standard: int):
    # queue 초기화
    queue = deque()
    queue.append([x, y])
    # 현재 위치 방문처리
    visited[x][y] = True

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 상, 하, 좌, 우 위치 체크
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 주어진 범위를 벗어나는지 체크 & 첫 방문인지 체크
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and graph[nx][ny] > standard:
                queue.append([nx, ny])
                visited[nx][ny] = True  # 방문처리


if __name__ == '__main__':
    # 첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다.
    n = int(input())
    # 둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다
    graph = [list(map(int, input().split())) for _ in range(n)]
    # 입력값 중 최대값
    max_value = max(map(max, graph))
    # 안전 영역
    safe = []

    for i in range(max_value):
        # 현재 반복문에서의 안전 영역
        area = 0
        # 방문처리를 담은 list
        visited = [[False] * n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if graph[x][y] > i and visited[x][y] == False:
                    bfs(x, y, i)
                    area += 1
        safe.append(area)

    print(max(safe))