# https://school.programmers.co.kr/learn/courses/30/lessons/120852
# programmers, level0: 소인수분해, python3
def factorization(n: int) -> set:
    result = set()
    num = 2

    while num <= n:
        if n % num == 0:
            result.add(num)
            n /= num
        else:
            num += 1

    return result

def solution(n: int) -> list:
    return sorted(factorization(n))

if __name__ == '__main__':
    print(solution(12))   # [2, 3]
    print(solution(17))   # [17]
    print(solution(420))  # [2, 3, 5, 7]