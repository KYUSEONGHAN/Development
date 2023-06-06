from typing import List


def solution(numbers: List[int], n: int) -> int:
    answer = 0

    for num in numbers:
        answer += num
        if answer > n:
            break

    return answer
