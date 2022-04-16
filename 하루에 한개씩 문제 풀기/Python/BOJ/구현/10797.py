# https://www.acmicpc.net/problem/10797
# boj, 10797: 10부제, python3
import sys

input = sys.stdin.readline

def solve(day: int, bunhos: list) -> int:
    return sum([1 for bunho in bunhos if bunho == day])

if __name__ == '__main__':
    day = int(input())
    bunhos = list(map(int, input().split()))

    print(solve(day, bunhos))