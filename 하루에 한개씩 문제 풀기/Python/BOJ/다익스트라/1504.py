# https://www.acmicpc.net/problem/1504
# boj, 1504: 특정한 최단 경로, python3
import heapq  # 다익스트라를 구현하기위해 heapq 모듈 import
import sys

# 입력의 범위가 넓어서 readline으로 입력 속도 향상
input = sys.stdin.readline
inf = int(1e9)  # 무한을 의미하는 값으로 임시로 10억을 설정

# 1번 정점에서 N번 정점으로 최단 거리로 이동하므로 1로 set
def dijkstra(k:int) -> list:
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [inf] * (n + 1)
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

    return distance

def solve() -> int:
    result = []

    # 다익스트라 알고리즘 수행
    lenth = dijkstra(1)
    lenth_v1 = dijkstra(v1)
    lenth_v2 = dijkstra(v2)

    # (1 => v1 => v2 => n), (1 => v2 => v1 => n)
    result.append(lenth[v1] + lenth_v1[v2] + lenth_v2[n])
    result.append(lenth[v2] + lenth_v1[n] + lenth_v2[v1])

    # 두 개의 정점을 지나는 최단 경로의 길이를 출력
    # 그러한 경로가 없을 때에는 -1을 출력
    return min(result) if min(result) < inf else -1


if __name__ == '__main__':
    # 정점의 개수 n과 간선의 개수 e
    n, e = map(int, input().split())
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트르 만들기
    graph = [[] for _ in range(n+1)]
    result = []

    # 모든 간선 정보를 입력받기
    for _ in range(e):
        a, b, c = map(int, input().split())
        # a번 정점에서 b정점까지 가는 거리(비용)가 c라는 의미
        graph[a].append([b, c])
        # 양방향 길이므로
        graph[b].append([a, c])

    # 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다
    v1, v2 = map(int, input().split())

    print(solve())