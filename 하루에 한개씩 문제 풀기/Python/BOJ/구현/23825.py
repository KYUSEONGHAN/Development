# https://www.acmicpc.net/problem/23825
# boj, 23825: sasa 모형을 만들어보자, python3
import sys

input = sys.stdin.readline

def solve(num1: int, num2: int) -> int:
    return min(num1, num2) // 2

if __name__ == '__main__':
    n, m = map(int, input().split())

    print(solve(n, m))