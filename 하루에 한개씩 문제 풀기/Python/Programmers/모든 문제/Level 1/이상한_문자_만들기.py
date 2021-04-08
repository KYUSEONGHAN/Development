# programmers, phase1 : 이상한 문자 만들기, python3
def solution(s):
    s = s.split(' ')
    cnt = 1
    result = ''

    for i in s:
        for j in i:
            if cnt % 2 != 0:
                j = j.upper()
            else:
                j = j.lower()
            result += j
            cnt += 1
        result += ' '
        cnt = 1

    return result[:-1]

# 최적코드
#  rhdudals0659 님 코드 참고
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
