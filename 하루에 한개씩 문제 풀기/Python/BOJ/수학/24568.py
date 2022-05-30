# https://www.acmicpc.net/problem/24568
# boj, 24568: cupcake party , python3
import sys

input = sys.stdin.readline

def solve(r:int, s:int) -> int:
    return (r * 8 + s * 3) - 28 if (r * 8 + s * 3) > 28 else 0

if __name__ == '__main__':
    r = int(input())
    s = int(input())

    print(solve(r, s))