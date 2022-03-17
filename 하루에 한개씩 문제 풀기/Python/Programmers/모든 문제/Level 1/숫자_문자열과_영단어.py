# https://programmers.co.kr/learn/courses/30/lessons/81301
# programmers, level1: 숫자 문자열과 영단어, python3
# 2021 카카오 채용연계형 인턴쉽
def solution(s):
    dict = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    for k, v in dict.items():
        s = s.replace(k, v)

    return int(s)
