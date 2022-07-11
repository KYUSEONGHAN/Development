# https://www.acmicpc.net/problem/25314
# boj, 25314: 코딩은 체육과목 입니다. python3
import sys

input = sys.stdin.readline

# 정수 자료형의 이름을 구하는 함수
def solve(n: int) -> str:
    return 'long ' * (n // 4) + 'int'

if __name__ == '__main__':
    n = int(input())

    print(solve(n))