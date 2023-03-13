# https://school.programmers.co.kr/learn/courses/30/lessons/120878
# programmers, level0: 유한소수 판별하기, python3
from math import gcd

def solution(a: int, b: int) -> int:
    b //= gcd(a, b)

    while b % 2 == 0:
        b //= 2

    while b % 5 == 0:
        b //= 5

    return 1 if b == 1 else 2

if __name__ == '__main__':
    print(solution(7, 20))   # 1
    print(solution(11, 22))  # 1
    print(solution(12, 21))  # 2