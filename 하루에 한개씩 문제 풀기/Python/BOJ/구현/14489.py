# https://www.acmicpc.net/problem/14489
# boj, 14489: 치킨 두 마리 (...), python3
import sys

input = sys.stdin.readline  # 변수 입력속도 향상

# 욱재가 치킨 두 마리를 살 수 있는지 알려주는 함수
def solve(bank1, bank2, target):
    money, chicken_price = bank1 + bank2, target * 2

    return money if money < chicken_price else money - chicken_price

if __name__ == '__main__':
    a, b = map(int, input().split())  # 통장의 잔고 a, b
    c = int(input())  # 치킨 한 마리의 가격 c

    print(solve(a, b, c))