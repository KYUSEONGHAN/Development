# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# programmers, level2: 게임 맵 최단거리, Python3
from collections import deque

# 이동방향 정의
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x: int, y: int, maps: list, visited: list):
    # queue 초기화
    queue = deque()
    queue.append([x, y])
    # 현재 위치 방문 처리
    visited[x][y] = True

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 이동방향 체크
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 주어진 범위를 벗어나는지 확인 & 첫 방문인지 체크 & 벽이면 무시하기
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visited[nx][ny] == False and maps[nx][ny] == 1:
                visited[nx][ny] = True  # 방문처리
                maps[nx][ny] = maps[x][y] + 1
                queue.append([nx, ny])

    return maps[len(maps)-1][len(maps[0])-1]

def solution(maps: list) -> int:
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]

    answer = bfs(0, 0, maps, visited)

    return answer if answer != 1 else -1

if __name__ == '__main__':
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))  # 11
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))  # -1