# https://www.acmicpc.net/problem/16395
# boj, 16395: 파스칼의 삼각형, python3
import sys

input = sys.stdin.readline

def dp(n, k):
    # 앞서 계산된 결과를 저장하기 위한 dp 테이블 초기화
    d = [[1 for _ in range(i)] for i in range(1, 31)]

    # DP bottom-up
    for i in range(2, n+1):
        for j in range(1, i):
            d[i][j] = d[i-1][j-1] + d[i-1][j]

    return d[n-1][k-1]

if __name__ == '__main__':
    n, k = map(int, input().split())

    print(dp(n, k))