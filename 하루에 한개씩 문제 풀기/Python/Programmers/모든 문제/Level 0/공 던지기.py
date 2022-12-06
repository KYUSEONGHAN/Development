# https://school.programmers.co.kr/learn/courses/30/lessons/120843
# programmers, level0: 공 던지기, python3
def solution(numbers: list, k: int) -> int:
    return numbers[(k-1) * 2 % len(numbers)]

if __name__ == '__main__':
    print(solution([1, 2, 3, 4], 2))  # 3
    print(solution([1, 2, 3, 4, 5, 6], 5))  # 3
    print(solution([1, 2, 3], 3))  # 2