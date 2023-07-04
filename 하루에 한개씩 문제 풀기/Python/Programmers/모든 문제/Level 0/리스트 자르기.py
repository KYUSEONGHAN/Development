from typing import List


def solution(n: int, slicer: List[int], num_list: List[int]) -> List[int]:
    a, b, c = slicer

    if n == 1:
        return num_list[:b + 1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b + 1]
    elif n == 4:
        return num_list[a:b + 1:c]