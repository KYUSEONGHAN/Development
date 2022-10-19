# https://school.programmers.co.kr/learn/courses/30/lessons/120893
# programmers, level0: 대문자와 소문자, python3
def solution(my_string: str) -> str:
    return ''.join(map(str, [string.lower() if string.isupper() else string.upper() for string in my_string]))

if __name__ == '__main__':
    print(solution("cccCCC"))      # "CCCccc"
    print(solution("abCdEfghIJ"))  # "ABcDeFGHij"