# https://www.acmicpc.net/problem/1850
# boj, 1850: 최대공약수, Python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

# 주어진 두 수의 최대공약수를 반환하는 함수
def solve(num1: int, num2: int) -> str:
    # 유클리드 호제법을 이용한 최대공약수 구현
    while num2:
        num1, num2 = num2, num1 % num2

    return num1 * '1'

if __name__ == '__main__':
    a, b = map(int, input().split())

    print(solve(a, b))