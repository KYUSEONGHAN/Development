# https://www.acmicpc.net/problem/2693
# boj, 2693: n번째 큰 수, python3
import sys

input = sys.stdin.readline

# 각 테스트 케이스에 대해 3번째 큰 값을 반환하는 함수
def solve(a: list) -> int:
    return sorted(a, reverse=True)[2]

if __name__ == '__main__':
    t = int(input())  # t: 테스트 케이스의 개수

    for _ in range(t):
        a = list(map(int, input().split()))  # a: 배열, 원소 10개 공백 기준 입력

        print(solve(a))
