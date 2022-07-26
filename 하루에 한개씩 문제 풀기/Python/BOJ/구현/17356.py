# https://www.acmicpc.net/problem/17356
# boj, 17356: 욱 제, python3
import sys

input = sys.stdin.readline

def solve(a: int, b: int) -> float:
    m = (b - a) / 400
    return 1 / (1+10**m)

if __name__ == '__main__':
    a, b = map(int, input().split())  # a: 욱의 욱제력, b: 제의 욱제력

    print(solve(a, b))