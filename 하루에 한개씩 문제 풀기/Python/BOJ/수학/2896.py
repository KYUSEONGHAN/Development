# https://www.acmicpc.net/problem/2896
# boj, 2896: 무알콜 칵테일, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

# 주스가 얼만큼 남는지 반환하는 함수
def solve(a, b, c, i, j, k):
    ratio = min(a/i, b/j, c/k)

    return a - i * ratio, b - j * ratio, c - k * ratio

if __name__ == '__main__':
    a, b, c = map(int, input().split())  # a: 오렌지, b: 사과, c: 파인애플 주스의 양
    i, j, k = map(int, input().split())  # 칵테일을 만드는데 필요한 주스의 비율

    print(*solve(a, b, c, i, j, k))