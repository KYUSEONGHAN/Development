# https://www.acmicpc.net/problem/3187
# boj, 3187: 양치기 꿍, python3
from collections import deque

# 이동방향 정의
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 탐색 함수 정의
def bfs(x: int, y: int):
    # 양과 늑대의 수를 담은 변수 전역변수화
    global k, v
    # queue 초기화
    queue = deque()
    queue.append([x, y])
    # 현재 위치 방문 처리
    visited[x][y] = True
    # 울타리 영역 내 양과 늑대의 수를 담는 변수
    k_num, v_num = 0, 0

    # 현재 울타리 영역이 양이면 영역 내 양의 수 증감
    if fence[x][y] == 'k':
        k_num += 1
    # 현재 울타리 영역이 늑대이면 영역 내 늑대 수 증감
    if fence[x][y] == 'v':
        v_num += 1

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 이동방향 체크
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 주어진 범위를 벗어나는지 확인 & 첫 방문인지 체크 & 울타리가 아닌지 체크
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == False and fence[nx][ny] != '#':
                visited[nx][ny] = True  # 방문처리
                queue.append([nx, ny])
                if fence[nx][ny] == 'k':
                    k_num += 1
                if fence[nx][ny] == 'v':
                    v_num += 1
    # 같은 울타리 영역 안의 양들의 숫자가 늑대의 숫자보다 더 많을 경우 늑대가 전부 잡아먹힌다. 물론 그 외의 경우는 양이 전부 잡아먹히겠지만 말이다.
    if k_num and v_num:
        if k_num > v_num:
            v -= v_num
        else:
            k -= k_num


if __name__ == '__main__':
    # 입력의 첫 번째 줄에는 각각 영역의 세로와 가로의 길이를 나타내는 두 개의 정수 R, C (3 ≤ R, C ≤ 250)가 주어진다.
    r, c = map(int, input().split())
    # 다음 각 R줄에는 C개의 문자가 주어지며 이들은 위에서 설명한 기호들이다.
    # 빈 공간을 '.'(점)으로 나타내고 울타리를 '#', 늑대를 'v', 양을 'k'
    k, v = 0, 0  # 양과 늑대의 수를 담는 변수
    fence = []

    for x in range(r):
        tmp = list(input())
        for y in range(c):
            if tmp[y] == 'k':  # 현재 반복문 요소가 k이면 양의 수 증감
                k += 1
            if tmp[y] == 'v':  # 현재 반복문 요소가 v이면 늑대 수 증감
                v += 1
        fence.append(tmp)

    # 방문처리를 담는 List
    visited = [[False] * c for _ in range(r)]

    # 탐색 시작
    for x in range(r):
        for y in range(c):
            if fence[x][y] == 'k' or fence[x][y] == 'v':
                if not visited[x][y]:
                    visited[x][y] = True
                    bfs(x, y)

    # 살아남게 되는 양과 늑대의 수를 각각 순서대로 출력한다.
    print(k, v)