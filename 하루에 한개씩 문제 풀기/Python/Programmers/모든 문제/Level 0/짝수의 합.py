# https://school.programmers.co.kr/learn/courses/30/lessons/120831
# programmers, level0: 짝수의 합, python3
def solution(n: int) -> int:
    return sum([x for x in range(2, n+1, 2)])

if __name__ == '__main__':
    print(solution(10))  # 30
    print(solution(4))   # 6