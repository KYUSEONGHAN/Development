# https://www.acmicpc.net/problem/22193
# boj, 22193: multiply, python3
import sys

input = sys.stdin.readline

def solve(num1: int, num2: int) -> int:
    return num1 * num2

if __name__ == '__main__':
    n, m = map(int, input().split())
    num1 = int(input())
    num2 = int(input())

    print(solve(num1, num2))