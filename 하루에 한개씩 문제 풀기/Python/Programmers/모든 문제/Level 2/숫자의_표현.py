# programmers, phase2:숫자의 표현, python3
# 구현 알고리즘
def solution(n):
    answer = 0

    for i in range(1, n + 1):
        target = 0
        for j in range(i, n + 1):
            target += j

            if target == n:
                answer = answer + 1
                break
            if target > n:
                break

    return answer