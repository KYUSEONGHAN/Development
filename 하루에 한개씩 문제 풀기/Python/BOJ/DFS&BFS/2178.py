# https://www.acmicpc.net/problem/2178
# boj, 2178: 미로 탐색, python3
from collections import deque

n, m = map(int, input().split())
# 2차원 리스트 할당
graph = [list(map(int, input())) for i in range(n)]
# 상, 하, 좌, 우 이동 방향 정의
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y):
    # bfs 구현을 위해 queue 구현
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 상,하, 좌, 우
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 주어진 미로의 공간을 벗어난 경우 체크
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 이동할수 있는곳인지 아닌지 체크
            if graph[nx][ny] == 0:
                continue
            # 해당 노드(위치)를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

if __name__ == '__main__':
    print(bfs(0, 0))