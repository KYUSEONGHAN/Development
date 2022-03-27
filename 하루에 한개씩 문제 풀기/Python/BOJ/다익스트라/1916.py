# https://www.acmicpc.net/problem/1916
# boj, 1916: 최소비용 구하기, python3
import heapq  # 다익스트라를 구현하기위해 heapq 모듈 import
import sys

# 입력의 범위가 크므로 readline으로 입력 속도 향상
input = sys.stdin.readline
inf = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

def dijkstra(start: int, end: int) -> int:
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [inf] * (n + 1)
    # 우선순위 큐(힙) 선언
    queue = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(queue, (0, start))
    distance[start] = 0

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

    return distance[end]

if __name__ == '__main__':
    # 도시의 개수 n
    n = int(input())
    # 버스의 개수 m
    m = int(input())
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
    graph = [[] for _ in range(n+1)]

    # 버스의 정보 입력
    for _ in range(m):
        # 출발 도시의 번호 x, 도착지의 도시 번호 y, 버스 비용 z
        x, y, z = map(int, input().split())
        # x에서 y까지 가는 비용이 z라는 의미
        graph[x].append([y, z])

    start, end = map(int, input().split())

    # 다익스트라 알고리즘을 수행
    print(dijkstra(start, end))