# https://school.programmers.co.kr/learn/courses/30/lessons/17682
# programmers, level1: [1차] 다트 게임, python3
def solution(dartResult: str) -> int:
    n = ''
    score = []
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            n = int(n) ** 1
            score.append(n)
            n = ''
        elif i == 'D':
            n = int(n) ** 2
            score.append(n)
            n = ''
        elif i == 'T':
            n = int(n) ** 3
            score.append(n)
            n = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = score[-1] * -1

    return sum(score)

if __name__ == '__main__':
    print(solution("1S2D*3T"))    # 37
    print(solution("1D2S#10S"))   # 9
    print(solution("1D2S0T"))     # 3
    print(solution("1S*2T*3S"))   # 23
    print(solution("1D#2S*3S"))   # 5


# 3번
# 점수 합계
# 0 ~ 10 점 한번에
# 점수 부분은 s, d, t
# 1제곱, 2제곱, 3제곱
# *, #
# 스타면 해당 점수와 바로 직전 점수를 둘 다 2배로
# #이면 해당 점수는 마이너스가 된다