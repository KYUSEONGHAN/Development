from typing import List

def check_homework(n: int, bunho: List[int]) -> str:
    return ' '.join(map(str, [x for x in range(1, n+1) if x not in bunho]))

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    bunho = list(map(int, input().split()))
    print(f'#{test_case} {check_homework(n, bunho)}')