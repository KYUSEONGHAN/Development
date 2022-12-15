# https://school.programmers.co.kr/learn/courses/30/lessons/120821
# programmers, level0: 배열 뒤집기, python3
def solution(num_list: list) -> list:
    return num_list[::-1]

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5]))        # [5, 4, 3, 2, 1]
    print(solution([1, 1, 1, 1, 1, 2]))     # [2, 1, 1, 1, 1, 1]
    print(solution([1, 0, 1, 1, 1, 3, 5]))  # [5, 3, 1, 1, 1, 0, 1]