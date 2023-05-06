from typing import List

def get_average(score: List[int]) -> int:
    return sum([x if x >= 40 else 40 for x in score]) // 5

T = int(input())

for test_case in range(1, T + 1):
    score = list(map(int, input().split()))
    print(f'#{test_case} {get_average(score)}')