from typing import List


def solution(my_string: str) -> List[str]:
    alpha_dict = {chr(x): 0 for x in range(ord('A'), ord('Z') + 1)}
    alpha_dict.update({chr(x): 0 for x in range(ord('a'), ord('z') + 1)})

    for string in my_string:
        alpha_dict[string] += 1

    return list(alpha_dict.values())