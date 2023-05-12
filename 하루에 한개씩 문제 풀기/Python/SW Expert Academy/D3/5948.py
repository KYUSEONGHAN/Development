from itertools import combinations
from typing import List


def num_game(nums: List[int]) -> int:
    result = []

    for x in list(combinations(nums, 3)):
        if sum(x) not in result:
            result.append(sum(x))

    return sorted(result, reverse=True)[4]


T = int(input())

for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    print(f'#{test_case} {num_game(nums)}')