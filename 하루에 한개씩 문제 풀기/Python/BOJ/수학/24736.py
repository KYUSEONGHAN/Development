# https://www.acmicpc.net/problem/24736
# boj, 24736: football scoring, python3
import sys

input = sys.stdin.readline

def solve(scores1: list, scores2: list):
    football_points = [6, 3, 2, 1, 2]
    score1_result = sum([x*y for x, y in zip(football_points, scores1)])
    score2_result = sum([x*y for x, y in zip(football_points, scores2)])

    return score1_result, score2_result

if __name__ == '__main__':
    scores1 = list(map(int, input().split()))
    scores2 = list(map(int, input().split()))

    print(*solve(scores1, scores2))