# https://www.acmicpc.net/problem/18301
# boj, 18301: rats, python3
import sys

input = sys.stdin.readline

def solve(num1: int, num2: int, num3: int) -> int:
    return ((num1 + 1) * (num2 + 1)) // (num3 + 1) - 1

if __name__ == '__main__':
    n1, n2, n3 = map(int, input().split())

    print(solve(n1, n2, n3))