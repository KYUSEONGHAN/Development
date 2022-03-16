# https://programmers.co.kr/learn/courses/30/lessons/86051
# programmers, level1: 없는_숫자_더하기, python3

def solution(numbers):
    return sum([num for num in range(1, 10) if num not in numbers])
