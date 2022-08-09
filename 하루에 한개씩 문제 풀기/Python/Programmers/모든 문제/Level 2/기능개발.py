# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# programmers, level2: 기능개발, python3
from math import ceil

def solution(progresses: list, speeds: list) -> list:
    stack, answer = [], []

    # 올림을 구현하기 위해 math 모듈의 ceil 함수 사용
    # 배열에 있는 각 값마다의 배포하는 날을 구한 list
    baepo_day = [ceil((100-progresses[x]) / speeds[x]) for x in range(len(progresses))]

    # 위에서 구한 배포하는 날로 for 반복 순회
    for x in baepo_day:
        if not stack:  # stack에 값이 없다면 무조건 값 추가
            stack.append(x)
            continue
        if stack[0] < x:  # 스택에 있는 값의 첫번째 인덱스보다 크다면
            answer.append(len(stack))  # 현재 stack list의 길이를 answer에 추가한 뒤,
            stack = [x]  # stack list clear 후, 현재 요소 append
        else:
            stack.append(x)  # 그렇지 아니할시, stack에 현재 값 append

    answer.append(len(stack))  # 반복문을 순회한 뒤, 나머지 stack 값 길이만큼 추가

    return answer

if __name__ == '__main__':
    print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))      # [1, 3, 2]
    print(solution([99, 99, 99, 90, 90, 90], [1, 1, 1, 1, 1, 1]))      # [3, 3]
    print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]))   # [1,2,3]
    print(solution([93, 30, 55, 60, 40, 65], [1, 30, 5, 10, 60, 7]))   # [2,4]