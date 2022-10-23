# https://school.programmers.co.kr/learn/courses/30/lessons/120891
# programmers, level0: 369게임, python3
def solution(order: int) -> int:
    return sum([1 for x in str(order) if x in ['3', '6', '9']])

if __name__ == '__main__':
    print(solution(3))      # 1
    print(solution(29423))  # 2