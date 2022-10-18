# https://school.programmers.co.kr/learn/courses/30/lessons/120854
# programmers, level0: 배열 원소의 길이, python3
def solution(strlist: list) -> list:
    return [len(x) for x in strlist]

if __name__ == '__main__':
    print(solution(["We", "are", "the", "world!"]))  # [2, 3, 3, 6]
    print(solution(["I", "Love", "Programmers."]))   # [1, 4, 12]