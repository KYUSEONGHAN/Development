# https://www.acmicpc.net/problem/4504
# boj, 4505: 배수 찾기, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

# 목록에 있는 수가 n의 배수인지 아닌지를 구하는 함수
def solve(n:int, num: int) -> str:
    return f'{num} is a multiple of {n}.' if num % n == 0 else f'{num} is NOT a multiple of {n}.'

if __name__ == '__main__':
    n = int(input())

    while True:
        num = int(input())

        if num == 0:
            break

        print(solve(n, num))