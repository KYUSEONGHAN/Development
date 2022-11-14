# https://school.programmers.co.kr/learn/courses/30/lessons/120808
# programmers, level0: 분수의 덧셈, python3
from math import gcd

def lcm(x: int, y: int) -> int:
    return x * y // gcd(x, y)

def solution(denum1: int, num1: int, denum2: int, num2: int) -> list:
    num = lcm(num1, num2)
    denum = (denum1 * num // num1) + (denum2 * num // num2)
    giyak = gcd(num, denum)

    return [denum // giyak, num // giyak]


if __name__ == '__main__':
    print(solution(1, 2, 3, 4))
    print(solution(9, 2, 1, 3))