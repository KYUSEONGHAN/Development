# https://school.programmers.co.kr/learn/courses/30/lessons/120815
# programmers, level0: 피자 나눠 먹기 (2), python3
def solution(n: int) -> int:
    answer = 1

    while True:
        if (answer * 6) % n == 0:
            break
        answer += 1

    return answer

if __name__ == '__main__':
    print(solution(6))  # 1
    print(solution(10))  # 5
    print(solution(4))  # 2