# programmers, phase1 : 하샤드 수, python3
def solution(x):
    return x % sum(list(map(int, str(x)))) == 0