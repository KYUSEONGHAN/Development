# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# programmers, level0: 두 큐 합 같게 만들기, python3
from collections import deque

def solution(queue1: list, queue2: list) -> int:
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2, answer = sum(queue1), sum(queue2), 0

    for _ in range(len(queue1) * 3):
        if sum1 > sum2:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
        elif sum1 < sum2:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
        else:
            return answer
        answer += 1

    return -1

if __name__ == '__main__':
    print(solution([3, 2, 7, 2], [4, 6, 5, 1]))    # 2
    print(solution([1, 2, 1, 2], [1, 10, 1, 2]))   # 7
    print(solution([1, 1], [1, 5]))                # -1