from typing import List


def dasol_box(data: List[List[float]]) -> float:
    result = 0

    for i in data:
        p, x = i
        result += p * x

    return result


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    data = [list(map(float, input().split())) for _ in range(n)]
    print(f'#{test_case} {dasol_box(data)}')