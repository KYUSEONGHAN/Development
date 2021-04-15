# programmers, phase1 : 소수 만들기, python3
from itertools import combinations


def check_sosu(n):
    if n != 1:
        for i in range(2, n):
            if n % i == 0:
                return False
    else:
        return False

    return True


def solution(numbers):
    result = [sum(i) for i in list(combinations(numbers, 3))]

    return sum(1 for i in result if check_sosu(i))