# https://www.acmicpc.net/problem/1717
# boj, 1717: 집합의 표현, python3
import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)  # 런타임 에러를 피하기 위해 최대 재귀 깊이 재설정

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] == x:
        return x

    parent[x] = find_parent(parent, parent[x])

    return parent[x]  # 경로 압축 기법


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 더 작은 원소가 부모 노드가 되도록 구현
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == '__main__':
    # 집합의 개수 n, 연산의 개수 m
    n, m = map(int, input().split())
    # 부모 테이블 초기화
    parent = [x for x in range(n + 1)]

    # m개의 줄에는 각각의 연산이 주어진다.
    for _ in range(m):
        # x = 0 -> 합집합, x = 1 -> 포함되어 있는지를 확인하는 연산
        x, a, b = map(int, input().split())

        # 합집합은 a가 포함되어 있는 집합과 b가 포함되어 있는 집합을 합친다는 의미
        if x == 0:
            union_parent(parent, a, b)
        # a와 b가 포함되어 있는지를 확인하는 연산
        else:
            if find_parent(parent, a) == find_parent(parent, b):
                print('YES')
            else:
                print('NO')