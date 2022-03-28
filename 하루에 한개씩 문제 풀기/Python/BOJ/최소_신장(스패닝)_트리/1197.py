# https://www.acmicpc.net/problem/1197
# boj, 최소 스패닝 트리, python3
import sys

input = sys.stdin.readline  # 변수의 입력 범위가 크므로 입력 속도 향상을 위해 readline 사용
sys.setrecursionlimit(100000)  # 런타임 에러를 피하기 위해 최대 재귀 깊이 재설정

# 특정 원소가 속한 집합을 찾기
def find_parent(parent: list, x: int) -> int:
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent, parent[x])

    return parent[x]  # 경로 압축

# 두 원소가 속한 집합을 합치기
def union_parent(parent: list, a: int, b: int):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solve() -> int:
    # 최종 비용을 담는 변수
    result = 0

    # 간선을 하나씩 확인
    for edge in edges:
        c, a, b = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += c

    return result

if __name__ == '__main__':
    # 첫째 줄에 정점의 개수 v와 간선의 개수 e
    v, e = map(int, input().split())
    # 부모 테이블 초기화
    parent = [x for x in range(v+1)]
    # 모든 간선을 담을 리스트
    edges = []

    # 모든 간선에 대한 정보를 입력받기
    for _ in range(e):
        # 각 간선에 대한 정보를 나타내는 세 정수 a, b, c가 주어진다.
        # a번 정점과 b번 정점이 가중치 c인 간선으로 연결되어 있다는 의미.
        a, b, c = map(int, input().split())
        # 비용순으로 정렬하기 위해 첫 번째 원소를 비용으로 설정
        edges.append([c, a, b])

    # 간선을 비용순으로 정렬
    edges.sort()

    # 최소 스패닝 트리의 가중치를 출력
    print(solve())