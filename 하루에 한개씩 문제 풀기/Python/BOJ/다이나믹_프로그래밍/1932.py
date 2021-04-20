# boj, 1932 : 정수 삼각형, python
# dp : 큰 문제를 작은 문제로 나눠서 푸는 알고리즘
import sys

def DP(triangle):
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] = triangle[i-1][-1] + triangle[i][j]
            else:
                triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
    return max(triangle[n-1])

n = int(sys.stdin.readline())
triangle = [list(map(int, input().split())) for _ in range(n)]

print(DP(triangle))