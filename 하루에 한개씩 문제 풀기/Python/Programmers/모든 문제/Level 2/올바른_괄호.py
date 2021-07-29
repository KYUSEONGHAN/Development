# programmers, phase2:올바른 괄호, python3
def solution(s):
    answer, target = True, 0

    for x in s:
        if x == '(':
            target += 1
        else:
            target -= 1
        if target < 0:
            return False

    return target == 0