# https://school.programmers.co.kr/learn/courses/30/lessons/132267
# programmers, level1: 콜라 문제, python3
def solution(a: int, b: int, n: int) -> int:
    answer = 0

    while n >= a:
        answer += (n // a) * b
        n = (n // a) * b + (n % a)

    return answer

if __name__ == '__main__':
    print(solution(2, 1, 20))  # 19
    print(solution(3, 1, 20))  # 9