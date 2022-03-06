# https://www.acmicpc.net/problem/10953
# boj, 10953: a+b-6, python3
import sys

input = sys.stdin.readline

def solve(test_case: list):
    for x, y in test_case:
        print(x+y)

if __name__ == '__main__':
    t = int(input())
    test_case = [list(map(int, input().split(','))) for _ in range(t)]

    solve(test_case)