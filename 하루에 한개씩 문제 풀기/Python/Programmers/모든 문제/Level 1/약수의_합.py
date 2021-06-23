# programmers, phase1 : 약수의 합, pytho3
def get_divisor(n):
    n = int(n)
    divisors = []
    divisors_back = []

    for i in range(1, int(n ** (1/2)) + 1):
        if (n % i == 0):
            divisors.append(i)
            if (i != (n // i)):
                divisors_back.append(n // i)

    return divisors + divisors_back[::-1]

def solution(n):
    return sum(get_divisor(n))


# 최적코드
#  - , rhdudals0659 , - , 이은지 님 코드 참고
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])