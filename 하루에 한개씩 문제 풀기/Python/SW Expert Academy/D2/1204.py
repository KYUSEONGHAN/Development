from typing import List


def top_cnt_num(scores: List[int]) -> int:
    dict = {}

    for num in scores:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1

    return sorted(dict.items(), key=lambda x: (x[-1], x[0]), reverse=True)[0][0]


T = int(input())

for test_case in range(1, T + 1):
    test_case_num = int(input())
    scores = list(map(int, input().split()))
    print(f'#{test_case_num} {top_cnt_num(scores)}')