# https://www.acmicpc.net/problem/13301
# boj, 13301: 타일 장식물, python3
import sys

input = sys.stdin.readline

def dp(n):
    # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d = [0] * 81

    d[1] = 4
    d[2] = 6

    # DP bottom-up
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]

    return d[n]

if __name__ == '__main__':
    n = int(input())

    print(dp(n))