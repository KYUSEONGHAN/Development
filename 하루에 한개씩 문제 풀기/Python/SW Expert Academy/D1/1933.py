from typing import List


def get_yaksu(num: int) -> List[int]:
    yaksu_list = []

    for x in range(1, num + 1):
        if num % x == 0:
            yaksu_list.append(x)

    return yaksu_list


N = int(input())

print(*get_yaksu(N))