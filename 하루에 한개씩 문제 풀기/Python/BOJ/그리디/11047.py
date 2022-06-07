# https://www.acmicpc.net/problem/11047
# boj, 11047: 동전 0, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

def solve(coins: list, target: int) -> int:
    coins = list(reversed(coins))  # 동전의 가치 내림차순으로 재정렬
    cnt = 0  # 목표 가치를 만드는데 필요한 동전 개수의 최솟값

    for coin in coins:             # 동전 금액 list for 반복문으로 순회
        if coin <= target:         # 만약 동전 금액이 목표 금액보다 작거나 같다면
            cnt += target // coin  # 목표 값을 현재 동전값으로 나눈값을 개수에 +
            target %= coin         # 목표값을 현재 동전값으로 나눈 나머지값으로 할당

    return cnt

if __name__ == '__main__':
    n, k = map(int, input().split())       # n: 동전의 종류, k: 목표 가치
    ai = [int(input()) for _ in range(n)]  # ai: 동전의 가치가 오름차순으로 입력됨.

    print(solve(ai, k))