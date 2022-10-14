# https://school.programmers.co.kr/learn/courses/30/lessons/120826
# programmers, level 0: 특정 문자 제거하기, python3
def solution(my_string: str, letter: str) -> str:
    return my_string.replace(letter, '')

if __name__ == '__main__':
    print(solution("abcdef", "f"))  # "abcde"
    print(solution("BCBdbe", "B"))  # "Cdbe"