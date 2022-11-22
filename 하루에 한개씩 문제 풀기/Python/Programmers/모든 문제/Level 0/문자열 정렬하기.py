# https://school.programmers.co.kr/learn/courses/30/lessons/120850
# programmers, level0: 문자열 정렬하기 (1), python3
def solution(my_string: str) -> list:
    return sorted([int(x) for x in my_string if x.isdigit()])

if __name__ == '__main__':
    print(solution("hi12392"))
    print(solution("p2o4i8gj2"))
    print(solution("abcde0"))