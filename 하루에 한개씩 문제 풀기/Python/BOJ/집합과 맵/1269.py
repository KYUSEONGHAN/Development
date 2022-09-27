# https://www.acmicpc.net/problem/1269/
# boj, 1269: 대칭 차집합, python3
import sys

input = sys.stdin.readline

# 주어진 두 집합의 대칭 차집합의 원소의 개수를 반환하는 함수
def solve(set_a: set, set_b: set) -> int:
    return len(set_a - set_b) + len(set_b - set_a)

if __name__ == '__main__':
    a, b = map(int, input().split())  # 집합 a의 원소의 개수, 집합 b의 원소의 개수
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    print(solve(set_a, set_b))