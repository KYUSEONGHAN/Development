# programmers, phase2:소수 찾기, python3
# 완전 탐색 알고리즘
from itertools import permutations


def check_sosu(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
    else:
        return False
    return True


def solution(numbers):
    l = list(numbers)
    nums, nums_v2 = [], []
    target_num = ''

    for i in range(1, len(l) + 1):
        nums += list(permutations(l, i))

    for x in nums:
        for y in x:
            target_num += y
        nums_v2.append(int(target_num))
        target_num = ''

    nums_v2 = list(set(nums_v2))

    return sum([1 for x in nums_v2 if check_sosu(x) == True])