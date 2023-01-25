# https://www.acmicpc.net/problem/3184
# boj, 3184: 양, python3
from collections import deque

# 이동방향 정의
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x: int, y: int):
    # 양과 늑대의 수를 전역변수화
    global o, v
    # 울타리 영역 내 양의 수, 울타리 영역 내 늑대의 수
    area_o, area_v = 0, 0
    # queue 초기화
    queue = deque()
    queue.append([x, y])

    if yard[x][y] == 'o':  # 현재 그래프 순회 요소가 양이면 영역 내 양의 수 증감
        area_o += 1
    if yard[x][y] == 'v':  # 현재 그래프 순회 요소가 늑대이면 영역 내 늑대 수 증감
        area_v += 1

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 상, 하, 좌, 우 위치 체크
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 주어진 범위를 벗어나는지 확인
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == False and yard[nx][ny] != '#':
                if yard[nx][ny] == 'o':
                    area_o += 1
                if yard[nx][ny] == 'v':
                    area_v += 1
                visited[nx][ny] = True  # 방문처리
                queue.append([nx, ny])
    # 영역 안의 양의 수가 늑대의 수보다 많다면 이기고, 늑대를 우리에서 쫓아낸다. 그렇지 않다면 늑대가 그 지역 안의 모든 양을 먹는다.
    if area_o and area_v:
        if area_o > area_v:
            v -= area_v
        else:
            o -= area_o

if __name__ == '__main__':
    # 첫 줄에는 두 정수 R과 C가 주어지며(3 ≤ R, C ≤ 250), 각 수는 마당의 행과 열의 수를 의미한다.
    r, c = map(int, input().split())
    # 다음 R개의 줄은 C개의 글자를 가진다. 이들은 마당의 구조(울타리, 양, 늑대의 위치)를 의미한다.
    o, v = 0, 0
    # 글자 '.' (점)은 빈 필드를 의미하며, 글자 '#'는 울타리를, 'o'는 양, 'v'는 늑대를 의미한다.
    yard = []

    for x in range(r):
        data = list(input())
        for j in range(c):
            if data[j] == 'o':
                o += 1
            if data[j] == 'v':
                v += 1
        yard.append(data)

    # 그래프(마당) 방문처리를 담는 list
    visited = [[False] * c for _ in range(r)]

    # 탐색 시작
    for x in range(r):
        for y in range(c):
            if yard[x][y] == '0' or yard[x][y] == 'v':
                # 현재 위치가 방문하지 않았으면 방문처리 후 탐색 시작
                if not visited[x][y]:
                    visited[x][y] = True
                    bfs(x, y)

    # 하나의 줄에 아침까지 살아있는 양과 늑대의 수를 의미하는 두 정수를 출력한다.
    print(o, v)