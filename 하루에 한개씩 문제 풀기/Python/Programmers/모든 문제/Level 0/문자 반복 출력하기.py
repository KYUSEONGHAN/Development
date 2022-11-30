# https://school.programmers.co.kr/learn/courses/30/lessons/120825
# programmers, level0: 문자 반복 출력하기, Python3
def solution(my_string: str, n: int) -> str:
    return ''.join(map(str, [x * n for x in my_string]))

if __name__ == '__main__':
    print(solution("hello", 3))  # "hhheeellllllooo"