# programmers, phase2 : 가장 큰 수, python3
# 정렬 알고리즘
def solution(numbers):
    l = [str(x) for x in numbers]

    return str(''.join(sorted(l, key=lambda x: x * 3, reverse=True)))
