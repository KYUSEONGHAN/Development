# programmers, phase1 : 음양 더하기, python3
def solution(absolutes, signs):
    return sum([absolutes[i] if signs[i] == True else absolutes[i] * (-1) for i in range(len(absolutes))])