# https://school.programmers.co.kr/learn/courses/30/lessons/134240
# programmers, level1: 푸드 파이트 대회, python3
def solution(food: list) -> str:
    answer = ''

    for index, x in enumerate(food[1:], start=1):
        if x >= 2:
            answer += str(index) * (x // 2)

    if answer:
        answer += '0' + answer[::-1]

    return answer

if __name__ == '__main__':
    print(solution([1, 3, 4, 6]))  # "1223330333221"
    print(solution([1, 7, 1, 2]))  # "111303111"