# boj, 2004 : 조합 0의 개수, python3
# 정수론 및 조합론
import sys


def factorial(num):
    if num <= 1:
        return num
    return factorial(num - 1) * num


def solve(n, m):
    cnt = 0

    if n == m:
        return 0
    if m == 1:
        target = n
    else:
        target = factorial(n) // (factorial(n - m) * factorial(m))

    while True:
        if target % 10 != 0:
            break
        target = target / 10
        cnt += 1

    return cnt


n, m = map(int, input().split())

print(solve(n, m))


# 정답 코드
# 파이리썬의 파이썬님 코드 참고
# n!의 5 개수 세는 함수
def five_count(n):
    answer = 0
    while n != 0:
        n = n // 5
        answer += n
    return answer


# n!의 2 개수 세는 함수
def two_count(n):
    answer = 0
    while n != 0:
        n = n // 2
        answer += n
    return answer


n, m = map(int, input().split())

if m == 0:
    print(0)

else:
    print(min(two_count(n) - two_count(m) - two_count(n - m), five_count(n) - five_count(m) - five_count(n - m)))
