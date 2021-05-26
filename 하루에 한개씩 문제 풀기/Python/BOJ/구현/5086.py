# boj, 5086 : 배수와 약수, python3
# 수학, 구현
import sys


def solve():
    while True:
        num1, num2 = map(int, sys.stdin.readline().split())

        if num1 == 0 and num2 == 0:
            break

        if num2 % num1 == 0:
            print('factor')
        elif num1 % num2 == 0:
            print('multiple')
        else:
            print('neither')


solve()