# https://www.acmicpc.net/problem/14248
# boj, 14248: 점프 점프, python3
from collections import deque
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

def bfs(start: int) -> int:
    queue = deque()  # bfs 구현을 위해 queue 구현
    queue.append(start)
    graph[start] = True  # 현재 위치 방문처리

    # 큐가 빌 때까지 반복
    while queue:
        x = queue.popleft()

        # 현재 위치에서 왼쪽, 오른쪽 이동 체크
        for location in [x - ai[x], x + ai[x]]:
            # 이동한 위치가 처음 방문하면서 그래프를 벗어나지 않는경우
            if 0 <= location < n:
                if graph[location] == False:
                    queue.append(location)
                    graph[location] = True  # 방문처리

    # 그래프 방문처리가 된 돌의 총 개수 반환
    return sum([1 for x in graph if x])

if __name__ == '__main__':
    n = int(input())  # 돌다리의 돌 개수, 왼쪽부터 1부터 N번
    ai = list(map(int, input().split()))  # 위치에서 점프할 수 있는 거리
    graph = [False] * n  # 그래프 방문했는지 확인용 list
    s = int(input()) - 1  # 출발점, index는 0에서부터 시작하므로 -1

    print(bfs(s))  # bfs graph 탐색 수횅
