# https://www.acmicpc.net/problem/2338
# boj, 2338: 긴자리 계산, python3
import sys

input = sys.stdin.readline

def solve(num1, num2):
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    solve(a, b)