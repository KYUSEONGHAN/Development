from typing import List

def solve(nums: List[int]) -> str:
    return ' '.join(map(str, sorted(nums)))

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    print(f'#{test_case} {solve(nums)}')