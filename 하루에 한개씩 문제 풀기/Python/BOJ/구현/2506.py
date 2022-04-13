# https://www.acmicpc.net/problem/2506
# boj, 2506: 점수계산, python3
import sys

input = sys.stdin.readline

def solve(scores: list) -> int:
    sequence, result = 0, scores[0]

    for x in range(1, len(scores)):
        if scores[x] == 1 and scores[x-1]:
            sequence += 1
        if scores[x] == 1:
            result += scores[x] + sequence
        else:
            sequence = 0

    return result

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    print(solve(scores))