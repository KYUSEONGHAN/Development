# https://www.acmicpc.net/problem/14716
# boj, 14716: 현수막, python3
from collections import deque
import sys

input = sys.stdin.readline

# 이동방향 정의
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(x: int, y: int):
    # queue 초기화
    queue = deque()
    queue.append([x, y])
    # 현재 위치 방문 처리
    visited[x][y] = True
    data[x][y] = 0

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 이동방향 체크
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 주어진 범위를 벗어나는지 확인 & 첫 방문인지 체크 & 현수막 정보가 1인지 체크
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == False and data[nx][ny] == 1:
                visited[nx][ny] = True  # 방문처리
                queue.append([nx, ny])
                data[nx][ny] = 0


if __name__ == '__main__':
    # 첫 번째 줄에는 현수막의 크기인 M와 N가 주어진다. (1 ≤ M, N ≤ 250)
    m, n = map(int, input().split())
    # 두 번째 줄부터 M+1 번째 줄까지 현수막의 정보가 1과 0으로 주어지며, 1과 0을 제외한 입력은 주어지지 않는다.
    data = [list(map(int, input().split())) for _ in range(m)]
    # 현수막 방문처리를 담은 list
    visited = [[False] * n for _ in range(m)]
    # 글자 수
    cnt = 0

    for x in range(m):
        for y in range(n):
            if data[x][y] == 1:
                bfs(x, y)
                cnt += 1

    print(cnt)