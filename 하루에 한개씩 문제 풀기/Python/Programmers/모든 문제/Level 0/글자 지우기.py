from typing import List

def solution(my_string: str, indices: List[int]) -> str:
    result = ""
    for i in range(len(my_string)):
        if i not in indices:
            result += my_string[i]
    return result