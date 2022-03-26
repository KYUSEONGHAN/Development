# https://www.acmicpc.net/problem/1956
# boj, 1956: 운동, python3
import sys

input = sys.stdin.readline  # readline으로 입력 속도 향상
inf = int(1e9)  # 무한을 의미하는 값으로 임의로 10억을 설정

def floyd():
    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(1, v+1):
        for a in range(1, v+1):
            for b in range(1, v+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


def solve() -> int:
    result = inf

    for i in range(1, v+1):
        # 도로의 길이의 합이 가장 작은 사이클을 찾는문
        result = min(result, graph[i][i])

    # 운동 경로를 찾는 것이 불가능한 경우에는 -1을 출력
    return result if result != inf else -1


if __name__ == '__main__':
    # v개의 마을과 e개의 도로
    v, e = map(int, input().split())
    # 2차원 리스트(그래프)에 모든 값을 무한으로 초기화
    # 플로이드 워셜은 다익스트라와는 다르게 2차원 그래프로 할당
    graph = [[inf] * (v+1) for _ in range(v+1)]

    # 각 도로에따른 운동 정보를 입력받아, 그 값으로 초기화
    for _ in range(e):
        a, b, c = map(int, input().split())
        # a번 마을에서 b번 마을로 가는 거리가 c라는 의미
        graph[a][b] = c

    # 플로이드 워셜 알고리즘 수행
    floyd()

    # 정답 출력
    print(solve())