# https://school.programmers.co.kr/learn/courses/30/lessons/72411
# programmers, level 2: 메뉴 리뉴얼, python3
from itertools import combinations

def solution(orders: list, course: list) -> list:
    answer, dict = [], {}

    for x in course:
        for order in orders:
            for y in list(combinations(order, x)):
                y = sorted(y)
                key = ''.join(y)
                if key not in dict:
                    dict[key] = 1
                else:
                    dict[key] += 1

    for x in course:
        arr, max_value = [], 2
        for key, value in dict.items():
            if len(key) == x:
                if max_value < value:
                    arr = [key]
                    max_value = value
                elif max_value == value:
                    arr.append(key)
        for y in range(len(arr)):
            answer.append(arr[y])

    return sorted(answer)

if __name__ == '__main__':
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))  # ["AC", "ACDE", "BCFG", "CDE"]
    print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))  # ["ACD", "AD", "ADE", "CD", "XYZ"]
    print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))  # ["WX", "XY"]