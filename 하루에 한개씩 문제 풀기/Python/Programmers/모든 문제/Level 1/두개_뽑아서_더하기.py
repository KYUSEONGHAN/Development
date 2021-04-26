# 코드💻
# programmers, phase1 : 두 개 뽑아서 더하기, python
from itertools import combinations


def solution(numbers):
    answer = set()

    for i in list(combinations(numbers, 2)):
        answer.add(sum(i))

    return sorted(answer)



# 최적코드
# sean, 최성우,... 님 코드 참고
def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    return sorted(list(set(answer)))