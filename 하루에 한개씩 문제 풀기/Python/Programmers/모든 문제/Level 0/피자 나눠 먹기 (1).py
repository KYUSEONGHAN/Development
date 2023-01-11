# https://school.programmers.co.kr/learn/courses/30/lessons/120814
# programmers, level0: 피자 나눠 먹기 (1), python
from math import ceil

def solution(n: int) -> int:
    return ceil(n / 7)

if __name__ == '__main__':
    print(solution(7))   # 1
    print(solution(1))   # 1
    print(solution(15))  # 3