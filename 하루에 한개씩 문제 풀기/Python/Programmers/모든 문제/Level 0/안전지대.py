# https://school.programmers.co.kr/learn/courses/30/lessons/120866
# programmers, level0: 안전지대, python3
from collections import deque

# 이동방향 정의
dx = [-1, 1, 0 , 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

# 탐색 함수
def bfs(x: int, y: int, visited: list, board: list):
    # queue 초기화
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True  # 현재 위치 방문처리

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 상, 하, 좌, 우, 대각선 위치 체크
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 주어진 범위를 벗어나는지 체크 & 첫 방문인지 체크
            if 0 <= nx < len(board) and 0 <= ny < len(board) and visited[nx][ny] == False:
                visited[nx][ny] = True  # 방문처리
                # 현재 위치가 지뢰라면
                if board[nx][ny] == 1:
                    queue.append([nx, ny])
                # 현재 위치가 위험지역이라면
                else:
                    board[nx][ny] = -1

def solution(board: list):
    answer = 0
    # graph 방문처리를 담은 list
    visited = [[False] * len(board) for _ in range(len(board))]

    # n * n 정사각형 Graph
    for x in range(len(board)):
        for y in range(len(board)):
            # 현재 위치가 지뢰이고 첫 방문일시에
            if board[x][y] == 1 and visited[x][y] == False:
                bfs(x, y, visited, board)  # 탐색수행

    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 0:
                answer += 1

    return answer

if __name__ == '__main__':
    print(solution(
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
    ))  # 16
    print(solution(
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
    ))  # 13
    print(solution(
        [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
    ))  # 0