# https://school.programmers.co.kr/learn/courses/30/lessons/120911
# programmers, level0: 문자열 정렬하기 (2), python3
def solution(my_string: str) -> str:
    return ''.join(map(str, sorted([x.lower() for x in my_string])))

if __name__ == '__main__':
    print(solution("Bcad"))
    print(solution("heLLo"))
    print(solution("Python"))