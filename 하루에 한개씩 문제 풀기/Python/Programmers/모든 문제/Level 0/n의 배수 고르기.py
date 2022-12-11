# https://school.programmers.co.kr/learn/courses/30/lessons/120905
# programmers, level0: n의 배수 고르기, python3
def solution(n: int, numlist: list) -> list:
    return [num for num in numlist if num % n == 0]

if __name__ == '__main__':
    print(solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(solution(5, [1, 9, 3, 10, 13, 5]))
    print(solution(12, [2, 100, 120, 600, 12, 12]))