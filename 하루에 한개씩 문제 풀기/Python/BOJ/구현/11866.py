# boj, 11866: 요세푸스 문제 0, python3
from collections import deque
import sys

input = sys.stdin.readline

def solve(n, k):
    queue = deque()
    result = []

    for x in range(1, n+1):
        queue.append(x)

    while queue:
        for _ in range(k-1):
            queue.append(queue.popleft())
        result.append(queue.popleft())

    return ", ".join(map(str, result))

if __name__ == '__main__':
    n, k = map(int, input().split())

    print("<" + solve(n, k) + ">")