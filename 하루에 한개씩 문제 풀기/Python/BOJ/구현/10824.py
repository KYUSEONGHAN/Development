# https://www.acmicpc.net/problem/10824
# boj, 10824: 네 수, python3
import sys

input = sys.stdin.readline

def solve(a: str, b: str, c:str, d: str) -> int:
    return int(a+b) + int(c+d)

if __name__ == '__main__':
    a, b, c, d = map(str, input().split())

    print(solve(a, b, c, d))