# programmers, phase1 : 약수의 개수와 덧셈, python3
# 월간코드 챌린지 시즌2
def divisor(num):
    return [i for i in range(1, num//2 + 1) if num % i == 0]

def solution(left, right):
    return sum([i if len(divisor(i))%2 == 1 else -i for i in range(left,right+1)])