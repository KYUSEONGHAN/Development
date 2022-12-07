# https://school.programmers.co.kr/learn/courses/30/lessons/120851
# programmers, level0: 숨어있는 숫자의 덧셈 (1), python3
def solution(my_string: str) -> int:
    return sum([int(x) for x in my_string if x.isdigit()])

if __name__ == '__main__':
    print(solution("aAb1B2cC34oOp"))  # 10
    print(solution("1a2b3c4d123"))  # 16