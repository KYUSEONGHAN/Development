from itertools import permutations
from typing import List


def check_str(str1: str, str2: str) -> bool:
    diff = 1

    if str1 == str2:
        return False

    for x in range(len(str1)):
        if str1[x] != str2[x]:
            diff -= 1
            if diff < 0:
                return False
    return True


def solution(inputArray: List[str]) -> bool:
    for x in list(permutations(inputArray, len(inputArray))):
        correct = len(x) - 1
        for y in range(len(x) - 1):
            if check_str(x[y], x[y + 1]):
                correct -= 1
            if correct == 0:
                return True

    return False