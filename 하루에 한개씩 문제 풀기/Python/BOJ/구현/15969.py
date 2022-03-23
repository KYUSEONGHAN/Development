# https://www.acmicpc.net/problem/15969
# boj, 15969: 행복, python3
import sys

input = sys.stdin.readline

def solve(scores: list) -> int:
    return max(scores) - min(scores)

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    print(solve(scores))