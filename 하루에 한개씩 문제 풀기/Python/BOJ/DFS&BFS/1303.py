# https://www.acmicpc.net/problem/1303
# boj, 1303: 전쟁 - 전투, Python3
from collections import deque

# 이동방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS (너비 우선 탐색) 알고리즘
def bfs(x: int, y: int) -> int:
    queue = deque()  # queue 자료구조 선언
    queue.append([x, y])
    visited[x][y] = True  # 현재 위치 방문처리
    cnt = 1  # 병사 수를 담은 변수

    while queue:  # queue가 빌 때 까지 무한반복
        x, y = queue.popleft()
        for i in range(4):  # 상, 하, 좌, 우 방향 체크
            nx = x + dx[i]
            ny = y + dy[i]

            # 주어진 범위를 벗어나지않고, 첫 방문인 경우, 같은 색 옷 병사인 경우
            if 0 <= nx < m and 0  <= ny < n and visited[nx][ny] == False and colors[x][y] == colors[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = True  # 현재 위치 방문처리
                cnt += 1

    return cnt  # 병사 수 반환


if __name__ == '__main__':
    n, m = map(int, input().split())  # 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다.
    # 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다.
    colors = [list(str(input())) for _ in range(m)]
    visited = [[False] * n for _ in range(m)]  # 방문처리를 담은 list

    w_count, b_count = 0, 0  # 흰색 옷 병사 수, 파란색 옷 병사 수

    for y in range(m):
        for x in range(n):
            if not visited[y][x]: # 현재 위치가 첫 방문인 경우에만 탐색 수행
                cnt = bfs(y, x)  # 탐색 수행 결과로 얻은 병사 수 저장
                if colors[y][x] == 'W':  # 현재 탐색 수행 위치가 흰색 옷 병사이면
                    w_count += cnt ** 2  # 흰색 옷 병사 수 제곱배 (w_count += cnt ** 2  # 흰색 옷 병사 수 제곱배)
                else:
                    b_count += cnt ** 2

    # 첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다.
    print(w_count, b_count)
