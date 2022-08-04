# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# programmers, level2: 카펫, python3
def solution(brown: int, yellow: int) -> list:
    answer, block = [], brown + yellow

    for y in range(3, block):
        x = block // y

        if x * y == block and x >= y and (x-2) * (y-2) == yellow:
            return [x, y]


if __name__ == '__main__':
    print(solution(10, 2))   # [4, 3]
    print(solution(8, 1))    # [3, 3]
    print(solution(24, 24))  # [8, 6]
    print(solution(12, 4))   # [4, 4]
    print(solution(18, 6))   # [8, 3]