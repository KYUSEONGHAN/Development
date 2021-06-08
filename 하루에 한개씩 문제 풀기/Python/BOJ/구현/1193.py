# boj, 1193 : 분수찾기, python3
# 수학, 구현 알고리즘
import sys


def find_bunsu(x):
    target = 1

    while x > target:
        x -= target
        target += 1

    if target % 2 == 0:
        num1 = x
        num2 = target - x + 1
    else:
        num1 = target - x + 1
        num2 = x

    return f'{num1}/{num2}'


X = int(sys.stdin.readline())

print(find_bunsu(X))