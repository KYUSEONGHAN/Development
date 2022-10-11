# https://www.acmicpc.net/problem/24480
# boj, 24480: 알고리즘 수업 - 깊이 우선 탐색 2, python3
from sys import setrecursionlimit, stdin

setrecursionlimit(10**6)  # 최대 재귀 깊이 재설정
input = stdin.readline    # 변수 입력 속도 향상

def dfs(graph: list, visited: list, start: int):
    global visited_order
    visited[start] = visited_order  # 현재 위치 방문처리

    for x in graph[start]:        # graph 순회
        if not visited[x]:        # 현재 위치를 방문하지 않았다면
            visited_order += 1    # 방문 순서 증감 후 재귀호출
            dfs(graph, visited, x)

if __name__ == '__main__':
    n, m, r = map(int, input().split())  # n: 정점의 수, m: 간선의 수, r: 시작 정점
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)  # graph 방문 여부 할당한 list
    visited_order = 1      # 방문 순서 변수

    for _ in range(m):
        u, v = map(int, input().split())  # u, v: 간선 정보
        graph[u].append(v)  # 양방향 간선
        graph[v].append(u)

    for x in range(n+1):
        graph[x].sort(reverse=True)  # 인접 정점은 내림차순으로 방문한다

    dfs(graph, visited, r)  # dfs 알고리즘 수행

    for x in visited[1:]:  # graph의 방문 순서를 순차적으로 출력
        print(x)