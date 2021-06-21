# programmers, phase1 : 정수 내림차순으로 배치하기, python
def solution(n):
    answer = list(sorted(map(int, str(n)), reverse=True))

    return int("".join(map(str, answer)))


# 최적코드
# rhdudals0659 , - , Nulltable , Song Myung Ho , - 외 70 명 코드 참고
def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)))