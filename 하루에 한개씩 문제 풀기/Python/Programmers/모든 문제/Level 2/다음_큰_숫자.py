# programmers, phase2 : 다음 큰 숫자, python3
def solution(n):
    target = format(n, 'b')

    while True:
        n += 1

        if format(n, 'b').count('1') == target.count('1'):
            return n