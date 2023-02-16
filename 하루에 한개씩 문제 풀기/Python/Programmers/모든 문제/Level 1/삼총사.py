# https://school.programmers.co.kr/learn/courses/30/lessons/131705
# programmers, level1: 삼총사, python3
from itertools import combinations

def solution(number: list) -> int:
    return sum([1 for x in list(combinations(number, 3)) if sum(x) == 0])

if __name__ == '__main__':
    print(solution([-2, 3, 0, 2, -5]))  # 2
    print(solution([-3, -2, -1, 0, 1, 2, 3]))  # 5
    print(solution([-1, 1, -1, 1]))  # 0