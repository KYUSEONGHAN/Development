# https://school.programmers.co.kr/learn/courses/30/lessons/120853
# programmers, level0: 컨트롤 제트, python3
def solution(s: str) -> int:
    answer = []

    for x in s.split():
        if x != 'Z':
            answer.append(int(x))
        else:
            if answer:
                answer.pop()

    return sum(answer)

if __name__ == '__main__':
    print(solution("1 2 Z 3"))      # 4
    print(solution("10 20 30 40"))  # 100
    print(solution("10 Z 20 Z 1"))  # 1