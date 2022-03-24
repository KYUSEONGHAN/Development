# https://www.acmicpc.net/problem/11404
# boj, 11404: 플로이드, python3
import sys

input = sys.stdin.readline  # readline으로 입력 속도 향상
inf = int(1e9)  # 무한을 의미하는 값으로 임의로 10억을 설정

def floyd():
    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 수행된 결과를 출력
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 만약 i에서 j로 갈 수 없는 경우에는 그 자리에서 0을 출력한다
            if graph[i][j] == inf:
                graph[i][j] = 0
        print(*graph[i][1:])


if __name__ == '__main__':
    # 도시 = n, 버스 = m
    n = int(input())
    m = int(input())
    # 2차원 리스트(그래프)에 모든 값을 무한으로 초기화
    # 플로이드 워셜은 다익스트라와는 다르게 2차원 그래프로 할당
    graph = [[inf] * (n+1) for _ in range(n+1)]

    # 자기 자신에게 가는 비용은 0으로 초기화
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0

    # 각 버스에 대한 정보를 입력받아, 그 값으로 초기화
    for _ in range(m):
        # 시작 도시 a, 도착 도시 b, 필요한 비용 c
        a, b, c = map(int, input().split())
        # a도시에서 b도시까지 가는데 필요한 비용 c라는 의미
        graph[a][b] = min(graph[a][b], c)

    # 플로이드 워셜 알고리즘 수행
    floyd()