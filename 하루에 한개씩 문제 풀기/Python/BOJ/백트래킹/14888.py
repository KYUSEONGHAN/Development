# https://www.acmicpc.net/problem/14888
# boj, 14888: 연산자 끼워넣기, python3
from itertools import permutations
from collections import deque
import sys

input = sys.stdin.readline

def solve(n: int, a_list: list, operators: list) -> str:
    max_value, min_value = -1e9, 1e9  # 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.
    queue = deque(list(permutations(operators, len(operators))))

    while queue:
        now = queue.popleft()
        num = a_list[0]

        for x in range(1, n):
            if now[x-1] == '+':
                num += a_list[x]
            elif now[x-1] == '-':
                num -= a_list[x]
            elif now[x-1] == '*':
                num *= a_list[x]
            elif now[x-1] == '÷':
                num = num // a_list[x] if num >= 0 else (abs(num) // a_list[x]) * -1

        max_value, min_value = max(max_value, num), min(min_value, num)

    return '\n'.join(map(str, [max_value, min_value]))


if __name__ == '__main__':
    n = int(input())  # 수의 개수
    a_list = list(map(int, input().split()))  # A1, A2, ..., AN
    operator_nums = list(map(int, input().split()))  # 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
    operator, operators = ['+', '-', '*', '÷'], []

    for x in range(4):
        if operator_nums[x]:
           operators.extend(operator[x] * operator_nums[x])

    print(solve(n, a_list, operators))