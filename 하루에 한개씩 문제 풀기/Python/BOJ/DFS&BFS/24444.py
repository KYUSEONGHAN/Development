# https://www.acmicpc.net/problem/24444
# boj, 24444: 알고리즘 수업 - 너비 우선 탐색 1, python3
from collections import deque
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

def bfs(graph: list, visited: list, now: int):
    global visited_order
    queue = deque()     # bfs 구현을 위해 queue 구현
    queue.append(now)   # 큐 맨 뒤에 시작 정점 R을 추가한다.
    visited[now] = visited_order  # 현재 위치 방문 처리

    # queue가 빌 때까지 반복
    while queue:
        data = queue.popleft()

        for v in graph[data]:
            if not visited[v]:       # 방문하지 않은 간선일 시,
                visited_order += 1   # 방문 순서 증감 후, 방문 처리
                visited[v] = visited_order
                queue.append(v)


if __name__ == '__main__':
    n, m, r = map(int, input().split())  # n: 정점의 수, m: 간선의 수, r: 시작 정점
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)  # 그래프 방문 횟수 할당한 list
    visited_order = 1  # 방문 순서

    for _ in range(m):
        u, v = map(int, input().split())  # u, v: 간선 정보
        graph[u].append(v)  # 양방향 간선
        graph[v].append(u)

    for x in range(n+1):
        graph[x].sort()  # 인접 정점은 오름차순으로 방문한다.

    bfs(graph, visited, r)  # bfs 탐색 알고리즘 수행

    for x in visited[1:]:  # graph 방문 순서 순차적으로 출력
        print(x)
