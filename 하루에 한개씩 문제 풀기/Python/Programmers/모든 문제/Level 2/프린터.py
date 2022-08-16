# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# programmers, level2: 프린터, python3
from collections import deque

def solution(priorities: list, location: int) -> int:
    # 주어진 priorites listd의 값 들에 대한 위치를 각각 표시하기 위해 재정의 [위치, 데이터]
    priorities = [[index, data] for index, data in enumerate(priorities)]
    # queue: priorties를 deque로 할당, reloaction: 인쇄 우선순위로 인해 최후에 재정렬된 데이터를 담을 list
    queue, relocation, answer = deque(priorities), [], 1

    # queue가 존재할때까지 무한반복
    while queue:
        max_num = max([data for _, data in queue])  # 현재 queue에 있는 요소 중 최댓값을 담는 변수
        index, data = queue.popleft()  # index: 위치, data: 현재 요소 값

        if data == max_num:  # 현재 요소값이 최댓값이라면
            relocation.append([index, data])  # 재정의 list에 위치
        else:                # 그렇지 아니할시
            queue.append([index, data])  # 뒤로 보냄

    for data in relocation:  # 재배열된 list for문 반복문 순회
        if data == priorities[location]:  # 현재 요소와 원래 list의 location data 값이 같다면
            break
        else:
            answer += 1

    return answer

if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))         # 1
    print(solution([1, 1, 9, 1, 1, 1], 0))   # 5