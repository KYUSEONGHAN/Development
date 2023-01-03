# https://school.programmers.co.kr/learn/courses/30/lessons/120910
# programmers, level0: 세균 증식, python3
def solution(n: int, t: int) -> int:
    for x in range(t):
        n *= 2

    return n

if __name__ == '__main__':
    print(solution(2, 10))  # 2048
    print(solution(7, 15))  # 229376