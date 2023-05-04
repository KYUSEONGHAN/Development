from typing import List

def money_unbalance(n: int, money: List[int]) -> int:
    average_money = sum(money) / n
    return sum([1 for x in money if x <= average_money])

T = int(input())

for test_case in range(1, T + 1):
    n  = int(input())
    money = list(map(int, input().split()))
    print(f'#{test_case} {money_unbalance(n, money)}')