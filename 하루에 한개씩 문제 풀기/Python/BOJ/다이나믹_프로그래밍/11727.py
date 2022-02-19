# https://www.acmicpc.net/problem/11727
# boj, 11727: 2*n 타일링 2, python3
import sys

input = sys.stdin.readline

def dp(n):
    # 앞서 계산된 결과를 저장하기 위한 dp 테이블 초기화
    d = [0] * 1001

    d[1] = 1
    d[2] = 3

    # dp bottom-up
    for i in range(3, n+1):
        d[i] = (d[i-1] + d[i-2] * 2) % 10007

    return d[n]

if __name__ == '__main__':
    n = int(input())

    print(dp(n))