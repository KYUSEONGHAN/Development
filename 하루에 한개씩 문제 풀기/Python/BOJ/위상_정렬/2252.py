# https://www.acmicpc.net/problem/2252
# boj, 2252: 줄 세우기, python3
from collections import deque
import sys

input = sys.stdin.readline  # readline으로 입력 속도 향상

# 위상 정렬 함수
def topology_sort() -> str:
    # 알고리즘 수행 결과를 담을 리스트
    result = []
    # 큐 기능을 위한 deque 라이브러리 사용
    queue = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소 꺼내기
        now = queue.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                queue.append(i)

    return ' '.join(map(str, result))

if __name__ == '__main__':
    # n명의 학생, m: 키를 비교한 회수
    n, m = map(int, input().split())
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (n + 1)
    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
    graph = [[] for _ in range(n+1)]

    # 방향 그래프의 모든 간선 정보를 입력받기
    for _ in range(m):
        # 키를 비교한 두 학생의 번호 a, b가 주어진다.
        a, b = map(int, input().split())
        # 정점 a에서 b로 이동
        graph[a].append(b)
        # 진입차수를 1 증가
        indegree[b] += 1

    # 위상 정렬 수행
    print(topology_sort())