# https://www.acmicpc.net/problem/20254
# boj, 20254: site score, python3
import sys

input = sys.stdin.readline

def solve(Ur: int, Tr: int, Uo: int, To: int) -> int:
    return 56 * Ur + 24 * Tr + 14 * Uo + 6 * To

if __name__ == '__main__':
    Ur, Tr, Uo, To = map(int, input().split())

    print(solve(Ur, Tr, Uo, To))