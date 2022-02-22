# https://www.acmicpc.net/problem/11726
# boj, 11726: 2*n 타일링
import sys

input = sys.stdin.readline

def dp(n):
    # dp table 초기화
    d = [0] * 1001

    d[1] = 1
    d[2] = 2

    # dp bottom-up
    for i in range(3, n+1):
        d[i] = (d[i-1] + d[i-2]) % 10007

    return d[n]

if __name__ == '__main__':
    n = int(input())

    print(dp(n))