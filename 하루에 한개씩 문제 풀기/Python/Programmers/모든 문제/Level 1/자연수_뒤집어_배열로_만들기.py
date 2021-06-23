# programmers, phase 1: 자연수 뒤집어 배열로 만들기, python3
def solution(n):
    return list(reversed(list(map(int, str(n)))))