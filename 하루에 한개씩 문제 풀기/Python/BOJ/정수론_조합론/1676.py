# boj, 1676 : 팩토리얼 0의 개수, python3
# 정수론 및 조합론
import sys

def factorial(num):
    if num <= 1:
        return num
    return factorial(num-1) * num


def solve(num):
    l = list(reversed(str(factorial(num))))

    for i in range(len(l)):
        if l[i] != '0':
            return i
    return 0


N = int(sys.stdin.readline())

print(solve(N))