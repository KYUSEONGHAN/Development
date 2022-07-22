# https://www.acmicpc.net/problem/4880
# boj, 4880: 다음수, python3
import sys

input = sys.stdin.readline

def solve(num1: int, num2: int, num3: int):
    if num3 - num2 == num2 - num1:  # 등차수열인 경우
        return f'AP {num3 + num3 - num2}'
    return f'GP {num3 * (num3 // num2)}'  # 등비수열인 경우

if __name__ == '__main__':
    while True:
        a1, a2, a3 = map(int, input().split())

        if a1 == 0 and a2 == 0 and a3 == 0:
            break

        print(solve(a1, a2, a3))
