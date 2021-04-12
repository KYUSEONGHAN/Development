## boj, 1715 : 카드 정렬하기, python3
import sys
import heapq

N = int(input())
card = [int(sys.stdin.readline()) for _ in range(N)]

heapq.heapify(card)
result = 0

while len(card) is not 1:
    s = 0

    for i in range(2):
        s += heapq.heappop(card)

    result += s
    heapq.heappush(card, s)

print(result)