# https://www.acmicpc.net/problem/17069
# boj, 17069: 파이프 옮기기 2, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

# 파이프의 한쪽 끝을 (n, n)으로 이동시키는 방법의 개수를 구하는 함수  (→, ↘, ↓)
def solve(n: int, graph: list) -> int:
    d = [[[0] * 3 for _ in range(n)] for _ in range(n)]  # dp table 초기화
    d[0][1][0] = 1  # 0: 가로, 1: 세로, 2: 대각선

    for i in range(1, n):
        if graph[0][i] == 1:
            break
        else:
            d[0][i][0] = 1

    for i in range(1, n):
        for j in range(2, n):
            if not graph[i][j]:
                d[i][j][0] = d[i][j-1][0] + d[i][j-1][2]  # 가로
            if not graph[i][j]:
                d[i][j][1] = d[i-1][j][1] + d[i-1][j][2]  # 세로
            if not graph[i][j-1] and not graph[i-1][j] and not graph[i][j]:
                d[i][j][2] = d[i-1][j-1][1] + d[i-1][j-1][0] + d[i-1][j-1][2]

    return sum(d[-1][-1])

if __name__ == '__main__':
    n = int(input())  # 집의 크기
    graph = [list(map(int, input().split())) for _ in range(n)]  # 집의 상태

    print(solve(n, graph))