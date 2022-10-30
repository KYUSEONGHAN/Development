# https://school.programmers.co.kr/learn/courses/30/lessons/120887
# programmers, level0: k의 개수, python3
def solution(i: int, j: int, k: int) -> int:
    answer = 0

    for x in range(i, j + 1):
        answer += sum([1 for x in list(str(x)) if x == str(k)])

    return answer

if __name__ == '__main__':
    print(solution(1, 13, 1))   # 6
    print(solution(10, 50, 5))  # 5
    print(solution(3, 10, 2))   # 0