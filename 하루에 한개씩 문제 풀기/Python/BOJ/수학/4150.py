# https://www.acmicpc.net/problem/4150
# boj, 4150: 피보나치 수, python3
import sys

input = sys.stdin.readline

def solve(n: int) -> int:
    # dp table 할당을 위한 초기화
    d = [0] * (n+1)

    # f(1) = 1, f(2) = 1
    d[0], d[1] = 1, 1

    # f(2) 까지의 값이면 dp 수행하지말고 바로 값 return
    if n <= 1:
        return 1

    # dp bottom-up -> fibonacci 구현
    for x in range(1, n+1):
        d[x] = d[x-1] + d[x-2]

    return d[n-1]

if __name__ == '__main__':
    n = int(input())

    print(solve(n))