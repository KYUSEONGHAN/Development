from typing import List


def solve(money: int) -> List[int]:
    dict = {
        50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0
    }

    for key in dict:
        if money >= key:
            dict[key] += money // key
            money %= key

    return list(dict.values())


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    print(f'#{test_case}')
    print(*solve(n))