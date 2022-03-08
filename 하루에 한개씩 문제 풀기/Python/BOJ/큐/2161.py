# https://www.acmicpc.net/problem/2161
# boj, 2161: 카드1, python3
from collections import deque
import sys

input = sys.stdin.readline

def solve(n):
    queue = deque([x for x in range(1, n+1)])
    cnt = 1
    result = []

    while queue:
        if cnt % 2 == 1:
            x = queue.popleft()
            result.append(x)
        else:
            x = queue.popleft()
            queue.append(x)
        cnt += 1

    return result

if __name__ == '__main__':
    n = int(input())

    print(*solve(n))