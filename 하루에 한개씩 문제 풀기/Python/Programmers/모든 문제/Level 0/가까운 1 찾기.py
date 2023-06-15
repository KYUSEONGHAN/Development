from typing import List


def solution(arr: List[int], idx: int) -> int:
    for x in range(idx, len(arr)):
        if arr[x] == 1:
            return x

    return -1