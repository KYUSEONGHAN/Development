# https://www.acmicpc.net/problem/23795
# boj, 23795: 사장님 도박으 재미로 하셔야 합니다. python3
import sys

input = sys.stdin.readline

def solve(moneys: list) -> int:
    return sum(moneys)

if __name__ == '__main__':
    moneys = []

    while True:
        money = int(input())

        if money == -1:
            break

        moneys.append(money)


    print(solve(moneys))