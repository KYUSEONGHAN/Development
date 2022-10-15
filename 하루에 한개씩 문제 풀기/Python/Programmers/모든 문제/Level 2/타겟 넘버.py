# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# programmers, level2: 타겟 넘버, python3
from collections import deque

def solution(numbers: list, target: int) -> int:
    answer = 0
    queue = deque()  # bfs 구현을 위해 deque 구현
    queue.append([-numbers[0], 0])
    queue.append([numbers[0], 0])

    # queue가 빌 때까지 반복문 수행
    while queue:
        number, index = queue.popleft()
        index += 1

        if index == len(numbers):
            if number == target:
                answer += 1
        else:
            queue.append([number - numbers[index], index])
            queue.append([number + numbers[index], index])

    return answer

if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))  # 5
    print(solution([4, 1, 2, 1], 4))     # 2