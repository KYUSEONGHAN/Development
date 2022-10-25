# https://school.programmers.co.kr/learn/courses/30/lessons/120924/
# programmers, level0: 다음에 올 숫자, python3
def solution(common: list) -> int:
    if common[1] - common[0] == common[2] - common[1]:  # 등차
        return common[-1] + (common[1] - common[0])
    else:  # 등비
        return common[-1] * (common[1] // common[0])

if __name__ == '__main__':
    print(solution([1, 2, 3, 4]))  # 5
    print(solution([2, 4, 8]))     # 16