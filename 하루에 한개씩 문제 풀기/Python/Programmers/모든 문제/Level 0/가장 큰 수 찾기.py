# https://school.programmers.co.kr/learn/courses/30/lessons/120899
# programmers, level0: 가장 큰 수 찾기, python3
def solution(array: list) -> list:
    return [max(array), array.index(max(array))]

if __name__ == '__main__':
    print(solution([1, 8, 3]))        # [8, 1]
    print(solution([9, 10, 11, 8]))   # [11, 2]