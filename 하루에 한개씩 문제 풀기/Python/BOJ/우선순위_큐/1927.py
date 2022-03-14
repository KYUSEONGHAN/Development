# https://www.acmicpc.net/problem/1927
# boj, 1927: 최소 힙, python3
import heapq
import sys

input = sys.stdin.readline

def solve(orders):
    # 최소 힙을 구현하기 위해 heap 초기화
    heap = []

    for x in orders:
        # x가 자연수라면 배열에 x라는 값을 넣는 연산을 수행
        if x != 0:
            heapq.heappush(heap, x)
        # x가 0이라면
        else:
            # 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력
            if not heap:
                print(0)
            # 배멸에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 연산을 수행
            else:
                print(heapq.heappop(heap))


if __name__ == '__main__':
    n = int(input())
    x = [int(input()) for _ in range(n)]

    solve(x)