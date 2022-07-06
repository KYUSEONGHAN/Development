# https://www.acmicpc.net/problem/8974
# boj, 8974: 희주의 수학시험, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

# 희주가 대답해야할 정답을 구하는 함수
def solve(a: int, b: int) -> int:
    result = []

    # extand로 1차원 확장
    for x in range(1, b+1):
        result += [x] * x

    # a번째부터 b까지의 list합 슬라이싱
    return sum(result[a-1:b])

if __name__ == '__main__':
    a, b = map(int, input().split())

    print(solve(a, b))