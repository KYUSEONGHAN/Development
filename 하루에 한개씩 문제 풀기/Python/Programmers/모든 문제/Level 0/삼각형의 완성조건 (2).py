# https://school.programmers.co.kr/learn/courses/30/lessons/120868
# programmers, level0: 삼각형의 완성조건 (2), python
def solution(sides: list) -> int:
    return 2 * min(sides) - 1

if __name__ == '__main__':
    print(solution([1, 2]))  # 1
    print(solution([3, 6]))  # 5
    print(solution([11, 7]))  # 13