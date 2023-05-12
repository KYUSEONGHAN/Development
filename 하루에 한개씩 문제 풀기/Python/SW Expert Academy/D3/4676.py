from typing import List


def make_sound(word: str, h: int, nums: List[int]) -> str:
    dict, result = {}, ''

    for x in range(len(word) + 1):
        if x == 0:
            dict[x] = ''
        else:
            dict[x] = word[x - 1]

    for num in nums:
        dict[num] += '-'

    for value in dict.values():
        result += value

    return result


T = int(input())

for test_case in range(1, T + 1):
    word = str(input())
    h = int(input())
    nums = list(map(int, input().split()))
    print(f'#{test_case} {make_sound(word, h, nums)}')