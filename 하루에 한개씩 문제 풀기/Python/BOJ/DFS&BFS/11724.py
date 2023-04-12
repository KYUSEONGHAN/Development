# https://www.acmicpc.net/problem/11724
# boj, 11724: 연결 요소의 개수, python3
from collections import deque
import sys

input = sys.stdin.readline

def bfs(start, visited, graph):  # 무방향 그래프 탐색에서는 BFS(너비 우선 탐색)이 대체로 유리.
    queue = deque([])  # 자료구조 queue 초기화
    queue.append(start)
    visited[start] = True  # 현재 위치 방문처리

    while queue:  # 큐가 빌때까지 반복
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

if __name__ == '__main__':
    n, m = map(int, input().split())  # 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
    graph = [[] for _ in range(n+1)]  # 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n+1)  # 방문처리를 담은 list
    count = 0  # 연결 요수 개수 변수

    for i in range(1, n+1):  # 탐색 수행
        if not visited[i]:
            bfs(i, visited, graph)
            count += 1

    print(count)  # 연결 요소 개수 출력