# μ½λπ»
# programmers, phase1 : λ κ° λ½μμ λνκΈ°, python
from itertools import combinations


def solution(numbers):
    answer = set()

    for i in list(combinations(numbers, 2)):
        answer.add(sum(i))

    return sorted(answer)



# μ΅μ μ½λ
# sean, μ΅μ±μ°,... λ μ½λ μ°Έκ³ 
def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    return sorted(list(set(answer)))