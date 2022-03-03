# https://www.acmicpc.net/problem/2747
# boj, 2747: 피보나치 수, python3
import sys

input = sys.stdin.readline

def fibonacci(n):
    # dp table 초기화
    d = [0] * 46
    d[1] = 1

    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]

    return d[n]

if __name__ == '__main__':
    n = int(input())

    print(fibonacci(n))

