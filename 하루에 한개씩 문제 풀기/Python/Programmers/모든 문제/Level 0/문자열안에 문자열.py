# https://school.programmers.co.kr/learn/courses/30/lessons/120908
# programmers, level0: 문자열안에 문자열, python3
def solution(str1: str, str2: str) -> int:
    return 1 if str2 in str1 else 2

if __name__ == '__main__':
    print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))  # 1
    print(solution("ppprrrogrammers", "pppp"))        # 2