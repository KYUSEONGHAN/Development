# https://school.programmers.co.kr/learn/courses/30/lessons/120833
# programmers, level0: 배열 자르기, python3
def solution(numbers: list, num1: int, num2: int) -> list:
    return numbers[num1:num2+1]

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5], 1, 3))  # [2, 3, 4]
    print(solution([1, 3, 5], 1, 2))  # [3, 5]