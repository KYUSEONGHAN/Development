# https://www.acmicpc.net/problem/10826
# boj, 10826: 피보나치 수 4, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

# n번째 피보나치 수를 반환하는 함수
def solve(n: int) -> int:
    d = [0] * 10001  # dp table 초기화

    d[0], d[1] = 0, 1

    # dp bottom-up
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]

    return d[n]  # n번째 피보나치 수

if __name__ == '__main__':  # main함수 시작
    n = int(input())

    print(solve(n))