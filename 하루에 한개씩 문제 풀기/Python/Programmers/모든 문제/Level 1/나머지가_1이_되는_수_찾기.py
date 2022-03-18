# https://programmers.co.kr/learn/courses/30/lessons/87389
# programmers, level1: 나머지가 1이 되는 수 찾기, python3
def solution(n):
    answer = 2

    while True:
        if n % answer == 1:
            return answer
        answer += 1


if __name__ == '__main__':
    print(solution(10))  # 3
    print(solution(12))  # 11
