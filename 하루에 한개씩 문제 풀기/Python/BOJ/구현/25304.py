# https://www.acmicpc.net/problem/25304
# boj, 25304: 영수증, python3
import sys

input = sys.stdin.readline

# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 확인하는 함수
def solve(target, datas) -> str:
    return 'Yes' if target == sum([x[0] * x[1] for x in datas]) else 'No'

if __name__ == '__main__':
    x = int(input())  # x: 영수증에 적힌 총 금액
    n = int(input())  # n: 영수증에 적힌 구매한 물건의 종류의 수
    datas = [list(map(int, input().split())) for _ in range(n)]

    print(solve(x, datas))