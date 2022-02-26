# https://www.acmicpc.net/problem/1743
# boj, 1743: 음식물 피하기, python3
from sys import stdin, setrecursionlimit

input = stdin.readline
# 재귀 호출로인한 시간 초과를 피하기 위해 최대 재귀 깊이 재설정
setrecursionlimit(10**5)

n, m, k = map(int, input().split())
trash = [list(map(int, input().split())) for _ in range(k)]
graph = [['.' for _ in range(m)] for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = []

# 그래프에 입력받은 쓰레기 위치 설정
for x, y in trash:
    graph[x-1][y-1] = '#'

# 상, 하, 좌, 우 이동 방향 정의
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def dfs(x, y):
    # 현재 위치 방문처리
    visited[x][y] = True
    size = 1

    # 상, 하, 좌, 우 방향 체크
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 주어진 범위를 벗어난 경우 종료
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 이동한 방향이 처음 방문한 경우이며
        if visited[nx][ny] == False:
            # 쓰레기인 경우에만
            if graph[nx][ny] == '#':
                size += dfs(nx, ny)

    return size

for x in range(n):
    for y in range(m):
        # 현재 위치가 처음 방문하며 쓰레기가 있으면 dfs 수행.
        if visited[x][y] == False and graph[x][y] == '#':
            result.append(dfs(x, y))

# 가장 큰 쓰레기의 크기 출력
print(max(result))