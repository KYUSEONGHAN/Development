# https://school.programmers.co.kr/learn/courses/30/lessons/12985
# programmers, level2: 예상 대진표, python3
def solution(n: int, a: int, b: int) -> int:
    answer = 0

    while a != b:
        answer += 1

        a, b = (a + 1) // 2, (b + 1) // 2

    return answer

if __name__ == '__main__':
    print(solution(8, 4, 7))  # 3