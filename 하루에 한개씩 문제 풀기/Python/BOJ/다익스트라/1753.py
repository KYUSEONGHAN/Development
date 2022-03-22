# https://www.acmicpc.net/problem/1753
# boj, 1753: 최단 경로, python3
import heapq  # 다익스트라를 구현하기위해 heapq 모듈 import
import sys

# 입력의 범위가 넓어서 readline으로 입력 속도 향상
input = sys.stdin.readline
inf = int(1e9)  # 무한을 의미하는 값으로 10억을 설정


def dijkstra(k: int):
    # 우선순위 큐(힙)
    queue = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(queue, (0, k))
    distance[k] = 0

    # 큐가 비어있지 않다면
    while queue:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


if __name__ == '__main__':
    # 정점의 개수 v와 간선의 개수e
    v, e = map(int, input().split())
    # 시작 정점의 번호 k
    k = int(input())
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
    graph = [[] for _ in range(v + 1)]
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [inf] * (v + 1)

    # 모든 간선 정보를 입력받기
    for _ in range(e):
        x, y, z = map(int, input().split())
        # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
        graph[x].append((y, z))

    # 다익스트라 알고리즘을 수행
    dijkstra(k)

    # 수행된 결과를 출력
    for x in range(1, v+1):
        # 도달할 수 없는 경우 INF를 출력
        if distance[x] == inf:
            print('INF')
        # 도달할 수 있다면 최단 경로를 출력
        else:
            print(distance[x])