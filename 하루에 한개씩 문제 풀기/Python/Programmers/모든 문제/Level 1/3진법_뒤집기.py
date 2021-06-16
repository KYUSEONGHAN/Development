# programmers, phase1 : 3진법 뒤집기, python3
# 월간 코드 챌린지 시즌1
def solution(n):
    result = ''

    while n > 0:
        n, mod = divmod(n, 3)
        result += str(mod)

    return int(result, 3)