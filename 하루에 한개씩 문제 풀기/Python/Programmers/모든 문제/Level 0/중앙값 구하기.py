# https://school.programmers.co.kr/learn/courses/30/lessons/120811
# programmers, level0: 중앙값 구하기, python3
def solution(array: list) -> int:
    return sorted(array)[len(array) // 2]

if __name__ == '__main__':
    print(solution([1, 2, 7, 10, 11]))  # 7
    print(solution([9, -1, 0]))         # 0