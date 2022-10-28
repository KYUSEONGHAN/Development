# https://school.programmers.co.kr/learn/courses/30/lessons/120902
# programmers, level0: 문자열 계산하기, python3
def solution(my_string: str) -> str:
    return eval(my_string)

if __name__ == '__main__':
    print(solution("3 + 4"))  # 7