# 시간 초과 코드
# boj, 3273 : 두 수의 합, python3
# 투 포인터, 정렬
import sys


def solution(n, l, x):
    result = 0

    for i in range(n):
        for j in range(i + 1, n):
            if l[i] + l[j] == x:
                result += 1

    return result


n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

print(solution(n, sequence, x))



# 성공 코드
import sys


def solution(n, l, x):
    left, right = 0, n - 1
    result = 0

    while left < right:
        target = l[left] + l[right]

        if target == x:
            result += 1
            left += 1
        elif target < x:
            left += 1
        else:
            right -= 1
    return result


n = int(sys.stdin.readline())
sequence = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())

print(solution(n, sequence, x))