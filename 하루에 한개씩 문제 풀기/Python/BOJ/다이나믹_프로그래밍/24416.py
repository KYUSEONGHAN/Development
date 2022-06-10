# https://www.acmicpc.net/problem/24416
# boj, 24416: 알고리즘 수업 - 피보나치 수 1, python3
import sys

input = sys.stdin.readline

# 피보나치 수 재귀호출 함수
def fib(n: int) -> int:
    result = 0

    if n == 1 or n == 2:
        result += 1
        # return 1
        return result

    return fib(n-1) + fib(n-2)

# 피보나치 수 동적 프로그래밍 함수
def fibonacci(n: int) -> int:
    f = [0] * 41
    f[1], f[2] = 1, 1
    result = 1

    for i in range(3, n):
        f[i] = f[i-1] + f[i-2]
        result += 1

    # return f[n]
    return result

if __name__ == '__main__':
    n = int(input())

    print(fib(n))
    print(fibonacci(n))