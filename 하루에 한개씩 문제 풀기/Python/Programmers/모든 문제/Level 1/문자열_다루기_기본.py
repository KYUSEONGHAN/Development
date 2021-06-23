# programmers, phase1 : 문자열 다루기 기본, python
def solution(s):
    try:
        return all((any((len(s) == 4, len(s) == 6)), type(int(s)) == int))
    except:
        return False