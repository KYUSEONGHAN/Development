from typing import List


def change_box(n: int, q: int, box: List[List[int]]) -> str:
    nums = [0] * n

    for i in range(1, q + 1):
        start, end = box[i - 1]
        nums[start - 1:end] = [i] * (end - start + 1)

    return ' '.join(map(str, nums))


T = int(input())

for test_case in range(1, T + 1):
    n, q = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(q)]
    print(f'#{test_case} {change_box(n, q, data)}')