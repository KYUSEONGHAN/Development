# https://www.acmicpc.net/problem/16486
# boj, 16486: 운동장 한 바퀴, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

pi = 3.141592

# 운동장의 한 바퀴 둘레를 알아내는 함수
def solve(d1: int, d2: int) -> float:
    return (d1 + d2 * pi) * 2

if __name__ == '__main__':
    d1 = int(input())  # 가로의 길이
    d2 = int(input())  # 반지름의 길이

    print(solve(d1, d2))