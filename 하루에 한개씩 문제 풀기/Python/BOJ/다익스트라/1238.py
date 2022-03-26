# https://www.acmicpc.net/problem/1238
# boj, 1238: 파티, python3
import heapq  # 다익스트라를 구현하기위해 heapq 모듈 import
import sys

# 입력의 범위가 넓으므로 readline으로 입력 속도 향상
input = sys.stdin.readline
inf = int(1e9)  # 무한을 의미하는 값으로 임의로 10억을 설정

def dijkstra(start: int) -> list:
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [inf] * (n + 1)
    # 우선순위 큐(힙)
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

    return distance

def solve() -> int:
    result = 0

    # n명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생이 누구일지 반복문으로 다익스트라 알고리즘 수행
    for i in range(1, n + 1):
        # 집에서 x로 갈 수 있고, x에서 집으로 돌아올 수 있으므로 (i -> x, x -> i)의 소요시간을 얻어야 함
        # 가장 오래 걸리는 소요시간을 얻어야하므로 max
        result = max(result, dijkstra(i)[x] + dijkstra(x)[i])

    return result  # 소요시간 반환


if __name__ == '__main__':
    # n명의 학생, m개의 단방향 도로, x번 마을
    n, m, x = map(int, input().split())
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 1차원 리스트 초기화
    graph = [[] for _ in range(n+1)]

    # 모든 간선(도로) 정보 입력받기
    for _ in range(m):
        # 도로의 시작점 a, 도로의 끝점 b, 도로르르 지나는데 필요한 소요시간 t
        a, b, t = map(int, input().split())
        # a에서 b로 가는 비용(소요시간)이 t라는 의미
        graph[a].append([b, t])

    # 결과 출력
    print(solve())