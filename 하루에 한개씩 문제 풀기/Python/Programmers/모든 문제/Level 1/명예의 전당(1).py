# https://school.programmers.co.kr/learn/courses/30/lessons/138477
# programmers, level1: 명예의 전당(1), python3
def solution(k: int, score: list) -> list:
    answer = []

    for x in range(len(score)):
        l = sorted(score[:x+1])
        if len(l) <= k:
            answer.append(l[0])
        else:
            answer.append(l[-k])

    return answer

if __name__ == '__main__':
    print(solution(3, [10, 100, 20, 150, 1, 100, 200]))  # [10, 10, 10, 20, 20, 100, 100]
    print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))  # [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]