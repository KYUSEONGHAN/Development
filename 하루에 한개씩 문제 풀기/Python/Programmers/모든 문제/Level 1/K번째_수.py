# programmers, phase1 : k번째 수, python
def solution(array, commands):
    answer = []

    for i in commands:
        slicing = sorted(array[i[0] - 1:i[1]])
        answer.append(slicing[i[2] - 1])
    return answer