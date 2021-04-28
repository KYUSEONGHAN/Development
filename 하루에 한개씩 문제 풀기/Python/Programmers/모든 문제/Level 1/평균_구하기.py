# programmers, phase1 : 평균 구하기, python
def solution(arr):
    try:
        return sum(arr) / len(arr)
    except ZeroDivisionError:
        return 0