# https://www.acmicpc.net/problem/9084
# boj, 9084: 동전, python3
import sys

input = sys.stdin.readline  # python 변수 입력 속도 향상

# 동전의 종류가 주어질 때, 주어진 금액을 만드는 모든 방법을 세는 함수
def solve(coins: list, target: int) -> int:
    d = [0] * (target + 1)  # dp table 초기화
    d[0] = 1

    for coin in coins:      # 입력된 동전의 각 금액 list for 반복문 순회
        for x in range(1, target+1):
            if coin <= x:
                d[x] += d[x-coin]

    return d[target]

if __name__ == '__main__':
    t = int(input())      # 테스트 케이스의 개수

    for _ in range(t):    # 테스트 케이스만큼 반복
        n = int(input())  # 동전의 가지 수
        coins = list(map(int, input().split()))  # n가지 동전의 각 금액
        m = int(input())  # n가지 동전으로 만들어야 할 금액

        print(solve(coins, m))