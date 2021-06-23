# programmers, phase1 : 문자열 내 마음대로 정렬하기, python
def solution(strings, n):
    return list(sorted(strings, key = lambda x : (x[n], x.lower())))