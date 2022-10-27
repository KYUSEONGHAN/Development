# https://school.programmers.co.kr/learn/courses/30/lessons/120848
# programmers, level0: 팩토리얼, python3
def solution(n: int) -> int:
    d = [0] * 3628801  # dp table 할당
    d[1], result = 1, 1

    while True:
        if d[result] > n:
            return result - 1

        result += 1
        d[result] = result * d[result-1]

if __name__ == '__main__':
    print(solution(3628800))  # 10
    print(solution(7))  # 3