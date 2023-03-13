# https://school.programmers.co.kr/learn/courses/30/lessons/120897
# programmers, level0: 약수 구하기, python3
def solution(n):
    answer = []

    for i in range(1, n + 1):
        if (n % i == 0):
            answer.append(i)

    return answer