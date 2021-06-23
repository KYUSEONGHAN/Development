# programmers, phase1 : 수박수박수박수박수박수?, python3
def solution(n):
    answer = '수박'

    if n == 1:
        return str(answer[0])
    elif n % 2 == 0:
        return str(answer * (n // 2))
    return str(answer * (n // 2) + answer[0])


# 최적코드
# - , jay , 이준 , Ji Hoon Kim , - 외 28 명 님 코드 참고
def water_melon(n):
    s = "수박" * n
    return s[:n]