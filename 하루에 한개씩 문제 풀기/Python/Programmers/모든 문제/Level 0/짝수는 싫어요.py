# https://school.programmers.co.kr/learn/courses/30/lessons/120813
# programmers, level0: 짝수는 싫어요, python3
def solution(n: int) -> list:
    return [x for x in range(1, n+1) if x % 2 == 1]

if __name__ == '__main__':
    print(solution(10))   # [1, 3, 5, 7, 9]
    print(solution(15))   # [1, 3, 5, 7, 9, 11, 13, 15]