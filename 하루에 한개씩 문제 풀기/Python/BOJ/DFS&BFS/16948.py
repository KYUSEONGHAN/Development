# https://www.acmicpc.net/problem/16948
# boj, 16948: 데스 나이트, Python3
from collections import deque
import sys

input = sys.stdin.readline

# 이동방향 정의
# 데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

# BFS 너비 우선 탐색 함수
def bfs(x: int, y: int):
    # queue 초기화
    queue = deque()
    queue.append([x, y])
    # 현재 위치 방문 처리
    visited[x][y] = 1

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 이동방향 체크
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            # 주어진 범위를 벗어나는지 확인 & 첫 방문인지 체크
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                visited[nx][ny] = visited[x][y] + 1  # 방문처리
                queue.append([nx, ny])

# 첫째 줄에 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.
def move_num(move: int) -> int:
    return move - 1

if __name__ == '__main__':
    # 첫째 줄에 체스판의 크기 N(5 ≤ N ≤ 200)이 주어진다.
    n = int(input())
    # 둘째 줄에 r1, c1, r2, c2가 주어진다.
    r1, c1, r2, c2 = list(map(int, input().split()))
    # 체스판 방문처리 List
    visited = [[0] * n for _ in range(n)]

    # 체스판 탐색 시작
    bfs(r1, c1)

    print(move_num(visited[r2][c2]))