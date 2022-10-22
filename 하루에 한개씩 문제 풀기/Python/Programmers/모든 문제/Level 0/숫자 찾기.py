# https://school.programmers.co.kr/learn/courses/30/lessons/120904
# programmers, level0: 숫자 찾기, python3
def solution(num: int, k: int) -> int:
    return str(num).index(str(k)) + 1 if str(k) in str(num) else -1

if __name__ == '__main__':
    print(solution(29183, 1))   # 3
    print(solution(232443, 4))  # 4
    print(solution(123456, 7))  # -1