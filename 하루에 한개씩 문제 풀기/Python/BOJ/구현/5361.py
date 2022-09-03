# https://www.acmicpc.net/problem/5361
# boj, 5361: 전투 드로이드 가격, python3
import sys

input = sys.stdin.readline

def solve(testcase: list) -> float:
    price = [350.34, 230.90, 190.55, 125.30, 180.90]

    return sum([price[x] * testcase[x] for x in range(5)])

if __name__ == '__main__':
    t = int(input())  # 테스트 케이스의 개수

    for _ in range(t):
        testcase = list(map(int, input().split()))

        print('$%.2f'%solve(testcase))

