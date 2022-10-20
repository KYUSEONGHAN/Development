# https://school.programmers.co.kr/learn/courses/30/lessons/120890
# programmers, level0: 가까운 수, python3
def solution(array: list, n: int) -> int:
    return array[sorted([[index, abs(n-num), num] for index, num in enumerate(array)], key=lambda x: (x[1], x[-1]))[0][0]]

if __name__ == '__main__':
    print(solution([3, 10, 28], 20))    # 28
    print(solution([10, 11, 12], 13))   # 12