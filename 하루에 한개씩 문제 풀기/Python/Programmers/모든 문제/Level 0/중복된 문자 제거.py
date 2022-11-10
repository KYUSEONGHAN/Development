# https://school.programmers.co.kr/learn/courses/30/lessons/120888/
# programmers, level0: 중복된 문자 제거, python3
def solution(my_string: str) -> str:
    dict = {}

    for x in my_string:
        if x not in dict:
            dict[x] = 1

    return "".join(map(str, [x for x in dict]))

if __name__ == '__main__':
    print(solution("people"))
    print(solution("We are the world"))