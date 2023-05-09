from typing import List


def normal_num(pi: List[int]) -> int:
    cnt = 0

    for x in range(1, len(pi) - 1):
        if pi[x] != min(pi[x], pi[x - 1], pi[x + 1]) and pi[x] != max(pi[x], pi[x - 1], pi[x + 1]):
            cnt += 1

    return cnt


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    pi = list(map(int, input().split()))
    print(f'#{test_case} {normal_num(pi)}')
