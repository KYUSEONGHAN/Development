from typing import List

def max_score(k: int, score: List[int]) -> int:
    return sum(sorted(score, reverse=True)[:k])

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    print(f'#{test_case} {max_score(k, score)}')