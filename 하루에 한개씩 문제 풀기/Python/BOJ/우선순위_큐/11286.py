# https://www.acmicpc.net/problem/11286
# boj, 11286: 절댓값 힙, python3
import heapq  # 최소, 최댓값을 찾는 문제이므로 우선순위 큐 문제이다.
import sys

# n의 범위가 크므로 입력받는 속도를 향상시키기 위해
input = sys.stdin.readline

def solve(n: int):
    # 우선순위 큐를 구현하기 위해 힙 초기화
    heap = []

    for _ in range(n):
        num = int(input())

        # x가 0이 아니라면 배열에 x 값을 추가하는 연산을 수행
        if num != 0:
            heapq.heappush(heap, [abs(num), num])
        # x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 연산을 수행
        else:
            # 만약 배열이 비어 있는 경우이면 0을 출력
            if not heap:
                print(0)
            else:
                print(heapq.heappop(heap)[1])


if __name__ == '__main__':
    n = int(input())

    solve(n)