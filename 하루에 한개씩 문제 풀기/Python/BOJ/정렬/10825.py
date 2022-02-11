# https://www.acmicpc.net/problem/10825
# boj, 10825: 국영수, python3
import sys

input = sys.stdin.readline

def solve(score_list):
    result = sorted(score_list, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

    for i in result:
        print(i[0])

if __name__ == '__main__':
    n = int(input())
    score_list = []

    for _ in range(n):
        name, hangle, elg, math = map(str, input().split())
        score_list.append([name, hangle, elg, math])

    solve(score_list)