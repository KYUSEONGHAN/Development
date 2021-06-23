# programmers, phase1 : 문자열 내림차순으로 배치하기, python
def solution(s):
    return "".join(list(sorted(s, reverse = True)))