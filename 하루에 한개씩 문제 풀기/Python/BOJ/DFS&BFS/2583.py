# https://www.acmicpc.net/problem/2583
# boj, 2583: 영역 구하기, python3
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)  # recursionerror를 피하기 위한 재귀 깊이 변경

m, n, k = map(int, input().split())
coordinate = [list(map(int, input().split())) for _ in range(k)]
graph = [[0] * n for _ in range(m)]
count = 0
result = []

for i in coordinate:
    start_x, start_y, end_x, end_y = i
    for j in range(start_y, end_y):
        for k in range(start_x, end_x):
            graph[j][k] = 1

def dfs(x, y):
    global count
    # 주어진 영역에서만 재귀 함수 호출되도록 조건문 설정
    # if x <= -1 or x >= m or y <= -1 or y >= n:
    if x < 0 or x >= m or y < 0 or y >= n:
        return False

    # 현재 위치 노드가 사각형 영역이면 pass
    if graph[x][y] == 1:
        return False

    # 현재 위치 노드가 사각형 영역이 아닌 구역이면
    graph[x][y] = 1  # 방문했다고 처리
    count += 1
    # 상, 하, 좌, 우 재귀 함수 호출
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)

    return count


for x in range(m):
    for y in range(n):
        cnt = dfs(x, y)
        if cnt:
            result.append(cnt)
            count = 0

print(len(result))
print(*sorted(result))
