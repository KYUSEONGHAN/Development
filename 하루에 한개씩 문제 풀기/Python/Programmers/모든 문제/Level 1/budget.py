# 시간초과 코드
# programmers, phase1 : 예산, python3
from itertools import combinations


def solution(d, budget):
    if sum(d) == budget:
        return len(d)
    for i in range(len(d), 1, -1):
        for j in list(combinations(d, i)):
            if sum(j) == budget:
                return i


# 성공 코드


def solution(d, budget):
    d.sort()

    while budget < sum(d):
        d.pop()

    return len(d)