# programmers, phase2 : 최댓값과 최솟값, python3
# 구현 알고리즘
def solution(s):
    l = s.split(' ')
    convert_l = [int(x) for x in l]

    return f"{min(convert_l)} {max(convert_l)}"