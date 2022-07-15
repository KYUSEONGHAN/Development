# https://www.acmicpc.net/problem/25311
# boj, 25311: ucpc에서 가장 쉬운 문제 번호는?, python3
import sys

input = sys.stdin.readline

# 입력년도의 ucpc 예선의 출제진이 의도한 가장 쉬운 문제의 번호를 반환하는 함수
def solve(year: int) -> str:
    return 'A'

if __name__ == '__main__':
    y = int(input())  # y: ucpc 개최 연도

    print(solve(y))