# https://school.programmers.co.kr/learn/courses/30/lessons/120896
# programmers, level0: 한번만 등장한 문자, python3
def solution(s: str) -> str:
    answer = ''
    dict = {}

    for x in s:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1

    for x in dict:
        if dict[x] == 1:
            answer += x

    return ''.join(map(str, sorted(answer)))

if __name__ == '__main__':
    print(solution("abcabcadc"))
    print(solution("abdc"))
    print(solution("hello"))