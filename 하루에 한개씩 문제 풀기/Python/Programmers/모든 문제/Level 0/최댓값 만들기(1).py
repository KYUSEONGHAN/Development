# https://school.programmers.co.kr/learn/courses/30/lessons/120847
# programmers, level0: 최댓값 만들기(1), python3
def solution(numbers: list) -> int:
    sort_numbers = sorted(numbers, reverse=True)

    return sort_numbers[0] * sort_numbers[1]

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5]))        # 20
    print(solution([0, 31, 24, 10, 1, 9]))  # 744