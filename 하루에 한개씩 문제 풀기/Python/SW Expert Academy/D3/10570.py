from math import sqrt


def is_palindrome(num: int) -> bool:
    if str(num) != str(num)[::-1]:
        return False

    sqrt_num = int(sqrt(num))

    return sqrt_num * sqrt_num == num and str(sqrt_num) == str(sqrt_num)[::-1]

def palindrome(a: int, b: int) -> int:
    result = 0

    for x in range(a, b + 1):
        if is_palindrome(x):
            result += 1

    return result


T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'#{test_case} {palindrome(a, b)}')