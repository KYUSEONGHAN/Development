# https://school.programmers.co.kr/learn/courses/30/lessons/120862
# programmers, level0: 최댓값 만들기 2, python3
def solution(numbers: list) -> int:
    nums_sort = sorted(numbers)

    return max(nums_sort[-1] * nums_sort[-2], nums_sort[0] * nums_sort[1])

if __name__ == '__main__':
    print(solution([1, 2, -3, 4, -5]))          # 15
    print(solution([0, -31, 24, 10, 1, 9]))     # 240
    print(solution([10, 20, 30, 5, 5, 20, 5]))  # 600