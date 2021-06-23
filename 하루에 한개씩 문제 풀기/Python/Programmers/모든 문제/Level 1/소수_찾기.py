# programmers, phase1 : 소수 찾기, python3
def solution(n):
    Sieve_of_Eratosthenes = [False, False] + [True] * (n - 1)
    result = []

    for i in range(2, n + 1):
        if Sieve_of_Eratosthenes[i]:
            result.append(i)
        for j in range(2 * i, n + 1, i):
            Sieve_of_Eratosthenes[j] = False
    return len(result)


# 최적코드
#  dalint , - , - , Jinsu Lim , 1stjstyle 외 388 명 님 코드 참고
def solution(n):
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)