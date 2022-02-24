# https://www.acmicpc.net/problem/4963
# boj, 4964: 섬의 개수, python3
from sys import stdin, setrecursionlimit

# 재귀 호출로 인한 시간 초과를 피하기 위해 최대 재귀 깊이 재설정
setrecursionlimit(10**5)
input = stdin.readline

# 이동할 방향 정의
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def dfs(x, y):
    graph[x][y] = 0
    # 방향 체크
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        # 주어진 범위를 벗어나는 경우 종료
        if nx <= -1 or ny <= -1 or nx >= h or ny >= w:
            continue
        # 이동한 방향과 현재 위치의 색이 같으면 같은 영역 처리
        if graph[nx][ny] == 1:
            dfs(nx, ny)

    return False

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    result = 0

    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1:
                dfs(x, y)
                result += 1

    print(result)