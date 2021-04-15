# boj, 2748 : 피보나치 수 2, python3
import sys

n = int(sys.stdin.readline())


def fibonacci(num):
    num1, num2 = 0, 1

    if num <= 1:
        return num
    else:
        for i in range(1, num):
            result = num1 + num2
            num1, num2 = num2, num1 + num2
        return result


print(fibonacci(n))