# programmers, level2:큰 수 만들기, Python3
def solution(number, k):
    answer = []  # Stack

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return ''.join(answer[:len(answer) - k])