# https://school.programmers.co.kr/learn/courses/30/lessons/120809
# programmers, level0: 두 배 만들기, python3
def solution(numbers: list) -> list:
    return [num * 2 for num in numbers]

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5]))  # [2, 4, 6, 8, 10]
    print(solution([1, 2, 100, -99, 1, 2, 3]))  # [2, 4, 200, -198, 2, 4, 6]