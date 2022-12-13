# https://school.programmers.co.kr/learn/courses/30/lessons/120583
# programmers, level0: 중복된 숫자 개수, python3
def solution(array: list, n: int) -> int:
    return array.count(n)

if __name__ == '__main__':
    print(solution([1, 1, 2, 3, 4, 5], 1))  # 2
    print(solution([0, 2, 3, 4], 1))  # 0