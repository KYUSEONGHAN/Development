# https://www.acmicpc.net/problem/2667
# boj, 2667: 단지번호붙이기, python3
from sys import setrecursionlimit

# 재귀 호출로인한 시간 초과를 피하기 위해서
setrecursionlimit(100000)

def dfs(x, y):
    # 현재 위치 방문처리
    visited[x][y] = True
    global cnt

    # 상, 하, 좌, 우 방향 체크
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 주어진 지도의 영역을 벗어난 경우 체크
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # 이동한 방향이 처음 방문했으며 집이 있는 경우에만
        if visited[nx][ny] == False and graph[nx][ny] == 1:
            cnt += 1
            # 재귀호출
            dfs(nx, ny)

    return cnt

if __name__ == '__main__':
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    # 이동 방향 정의
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    cnt = 1  # 단지
    result = []

    # 그래프 탐색
    for x in range(n):
        for y in range(n):
            # 현재 위치를 처음 방문하며 집인 경우에만
            if visited[x][y] == False and graph[x][y] == 1:
                danji = dfs(x, y)
                if danji:
                    result.append(danji)
                    cnt = 1  # 단지내 집의 수 초기화


    print(len(result))  # 단지수 출력
    print('\n'.join(map(str, sorted(result))))
