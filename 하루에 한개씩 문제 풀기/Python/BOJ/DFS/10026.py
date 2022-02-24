# https://www.acmicpc.net/problem/10026
# boj, 10026: 적록색약, python3
from sys import stdin, setrecursionlimit

# 재귀 호출로인한 시간 초과를 피하기 위해서
setrecursionlimit(100000)
input = stdin.readline

n = int(input())
graph = [list(map(str, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
# 이동할 방향 정의
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
cnt = 0
result = []

def dfs(x, y):
    # 현재 위치 방문처리
    visited[x][y] = True

    # 상, 하, 좌, 우 방향 체크
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 주어진 범위를 벗어나는 경우 종료
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # 이동한 방향이 처음 방문한 경우일 때,
        if visited[nx][ny] == False:
            # 이동한 방향과 현재 위치의 색이 같으면 같은 영역 처리
            if graph[x][y] == graph[nx][ny]:
                dfs(nx, ny)

    return False

# 색맹이 아닐때와, 색맹인 경우 체크
for i in range(2):
    # 모든 위치 탐색
    for x in range(n):
        for y in range(n):
            # 현재 위치를 처음 방문하면 dfs 수행
            if visited[x][y] == False:
                dfs(x, y)
                cnt += 1
    result.append(cnt)
    cnt = 0

    # 두번째 반복문일 경우 아래 코드 무시
    if i == 1:
        break
    # 방문처리 초기화
    visited = [[False] * n for _ in range(n)]
    # 색맹인 경우 r==g여서 g = r
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 'G':
                graph[x][y] = 'R'

print(*result)