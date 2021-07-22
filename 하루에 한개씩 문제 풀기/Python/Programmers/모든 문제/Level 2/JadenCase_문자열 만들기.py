# programmers, phase2 : JadenCase 문자열 만들기, python3
def solution(s):
    answer = ''

    if type(s[0]) == str:
        answer += s[0].upper()
    else:
        answer += s[0]

    for x in range(1, len(s)):
        if s[x - 1] == ' ':
            answer += s[x][0].upper()
        else:
            answer += s[x][0].lower()

    return answer