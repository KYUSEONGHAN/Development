# programmers, phase2:N개의 최소공배수, python3
# 수학, 구현 알고리즘
def gcd(x, y):  # 최대공약수
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):  # 최소공배수
    return x * y // gcd(x, y)


def solution(arr):
    target = arr[0]

    for x in range(1, len(arr)):
        target = lcm(target, arr[x])

    return target