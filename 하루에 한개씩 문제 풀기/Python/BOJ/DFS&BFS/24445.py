# https://www.acmicpc.net/problem/24445
# boj, 24445: 알고리즘 수업 - 너비 우선 탐색 2, python3
from collections import deque
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

def bfs(graph: list, visited: list, start: int):
    global visited_order
    queue = deque()      # bfs 알고리즘을 구현하기위해 queue 구현
    queue.append(start)  # 큐에 시작 정점 r(start)를 추가
    visited[start] = visited_order  # 현재 위치 방문 처리

    # queue가 빌 때까지 반복문 수행
    while queue:
        now = queue.popleft()    # 큐 맨 앞쪽의 요소를 삭제

        for v in graph[now]:     # 정점 now의 인접 정점 집합.
            if not visited[v]:   # 방문하지 않았으면, 방문순서 증감 후, 방문처리
                visited_order += 1
                visited[v] = visited_order
                queue.append(v)  # 큐에 정점 v 추가


if __name__ == '__main__':
    n, m, r = map(int, input().split())  # n: 정점의 수, m: 간선의 수, r: 시작 정점
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    visited_order = 1  # 그래프 방문 순서 할당한 변수

    # 다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다.
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 인접 정점은 내림차순으로 방문한다.
    for x in range(n+1):
        graph[x].sort(reverse=True)

    # bfs 탐색 알고리즘 수행
    bfs(graph, visited, r)

    # graph의 방문 순서를 순차적으로 출력
    for x in visited[1:]:
        print(x)