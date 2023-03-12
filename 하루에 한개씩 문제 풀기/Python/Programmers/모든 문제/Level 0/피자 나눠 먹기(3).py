# https://school.programmers.co.kr/learn/courses/30/lessons/120816
# programmers, level0: 피자 나눠 먹기(3), python3
def solution(slice: int, n: int) -> int:
    answer, tmp = 1, slice

    while True:
        if slice / n >= 1:
            break
        slice += tmp
        answer += 1

    return answer