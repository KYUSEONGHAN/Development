# programmers, phase1 : 정수 제곱근 판별, python
from math import sqrt

def solution(n):
    return int(sqrt(n) + 1) ** 2 if sqrt(n) % 1 == 0 else -1