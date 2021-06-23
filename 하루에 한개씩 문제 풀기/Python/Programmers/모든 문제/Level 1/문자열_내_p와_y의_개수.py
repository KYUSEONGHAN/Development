# programmers, phase1 : 문자열 내 p와 y의 개수, python
def solution(s):
    return True if s.count('p') + s.count('P') == s.count('y') + s.count('Y') else False

# 최적 코드
# - , 임형섭 , Minje Jeon , temp , - 외 81 명 님 코드 참고
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')