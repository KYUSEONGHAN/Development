# https://school.programmers.co.kr/learn/courses/30/lessons/120836
# programmers, level0: 순서쌍의 개수, python3
def solution(n: int) -> int:
    return sum([1 for x in range(1, n+1) if n % x == 0])

if __name__ == '__main__':
    print(solution(20))   # 6
    print(solution(100))  # 9