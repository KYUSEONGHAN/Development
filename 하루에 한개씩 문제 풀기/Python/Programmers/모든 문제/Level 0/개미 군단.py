# https://school.programmers.co.kr/learn/courses/30/lessons/120837
# programmers, level0: 개미 군단, python3
def solution(hp: int) -> int:
    answer = 0

    answer += hp // 5
    hp %= 5

    answer += hp // 3
    hp %= 3

    answer += hp // 1

    return answer

if __name__ == '__main__':
    print(solution(23))  # 5
    print(solution(24))  # 6
    print(solution(999))  # 201