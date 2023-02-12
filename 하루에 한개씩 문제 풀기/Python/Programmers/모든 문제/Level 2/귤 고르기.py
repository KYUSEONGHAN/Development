# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# programmers, level2: 귤 고르기, python3
def solution(k: int, tangerine: list) -> int:
    answer, dict = 0, {}

    for x in tangerine:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1

    for key, value in sorted(dict.items(), key=lambda x:-x[-1]):
        k -= value
        answer += 1
        if k <= 0:   # 귤을 크기별로 분류했을 때, 서로 다른 종류의 수를 최소화
            return answer

if __name__ == '__main__':
    print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))  # 3
    print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))  # 2
    print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))  # 1