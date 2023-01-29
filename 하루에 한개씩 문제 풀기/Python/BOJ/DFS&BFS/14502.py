# https://www.acmicpc.net/problem/14502
# boj, 14502: 연구소, python3
from collections import deque
import sys
import copy

# 변수 입력 속도 향상
input = sys.stdin.readline

# 이동방향 정의
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 탐색 함수
def bfs():
    # 안전 영역 최대 크기 전역변수화
    global safe
    # queue 초기화
    queue = deque()
    map_copy = copy.deepcopy(map)
    for x in range(n):
        for y in range(m):
            # 현재 위치가바이러스이면
            if map_copy[x][y] == 2:
                queue.append([x, y])

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 상, 하, 좌, 우 위치 체크
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 주어진 범위를 벗어나는지 체크 & 빈칸인지 체크
            if 0 <= nx < n and 0 <= ny < m and map_copy[nx][ny] == 0:
                queue.append([nx, ny])
                map_copy[nx][ny] = 2  # 오염처리

    max_area_num = 0

    for x in range(n):
        for y in range(m):
            if map_copy[x][y] == 0:
                max_area_num += 1

    safe = max(safe, max_area_num)


# 새로 벽을 세우는 함수
def build_wall(wall_num: int):
    if wall_num != 3:
        for x in range(n):
            for y in range(m):
                if map[x][y] == 0:
                    map[x][y] = 1
                    build_wall(wall_num + 1)
                    map[x][y] = 0
    # 새로 지을 수 있는 벽의 최대 수가 되면 탐색 수행
    else:
        bfs()


if __name__ == '__main__':
    # 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
    n, m = map(int, input().split())
    # 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다.
    # 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다
    map = [list(map(int, input().split())) for _ in range(n)]
    # 안전 영역의 최대 크기를 담은 변수
    safe = 0
    # 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
    wall = 0

    # 벽 세우기 수행
    # 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.
    build_wall(wall_num=0)
    print(safe)