# programmers, phase1 : 두 정수 사이의 합, python
def solution(a, b):
    if a < b :
        return sum(list(range(a, b+1)))
    else:
        return sum(list(range(b, a+1)))



# 최적코드
# 임형섭 , Minje Jeon , freelunch , - 외 42명 코드 참고
def adder(a, b):
    return sum(range(min(a,b), max(a,b) + 1))