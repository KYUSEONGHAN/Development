# https://www.acmicpc.net/problem/24479
# boj, 24479: 알고리즘 수업 - 깊이 우선 탐색 1, python3
from sys import setrecursionlimit, stdin

# 재귀 호출로인한 시간 초과를 피하기 위함.
setrecursionlimit(10 ** 6)

# 변수 입력 속도 향상
input = stdin.readline


def dfs(graph: list, visited: list, now: int):
    global visit_order
    visited[now] = visit_order

    for x in graph[now]:
        if not visited[x]:
            visit_order += 1
            dfs(graph, visited, x)


if __name__ == '__main__':
    # n: 정점의 수, m: 간선의 수, r: 시작 정점
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    visit_order = 1
    # 다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다.
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 정점 번호를 오름차순으로 방문한다
    for x in range(n + 1):
        graph[x].sort()

    # dfs 알고리즘 수행
    dfs(graph, visited, r)

    # 각 방문한 방문 순서 출력
    for x in range(1, n + 1):
        print(visited[x])