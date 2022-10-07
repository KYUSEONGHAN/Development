# https://www.acmicpc.net/problem/15652
# boj, 15652: n과 m (4), python3
import sys

input = sys.stdin.readline

def solve(n: int, m: int, graph: list, start: int):
    if len(graph) == m:
        print(' '.join(map(str, graph)))
        return

    for x in range(start, n+1):
        graph.append(x)
        solve(n, m, graph, x)
        graph.pop()

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = []

    solve(n, m, graph, 1)