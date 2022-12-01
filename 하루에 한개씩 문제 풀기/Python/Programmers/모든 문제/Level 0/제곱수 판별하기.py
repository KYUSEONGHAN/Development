# https://school.programmers.co.kr/learn/courses/30/lessons/120909
# programmers, level0: 제곱수 판별하기, python3
from math import sqrt

def solution(n: int) -> int:
    return 1 if sqrt(n) == int(sqrt(n)) else 2

if __name__ == '__main__':
    print(solution(144))  # 1
    print(solution(976))  # 2