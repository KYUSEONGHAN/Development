# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# programmers, level2: 주식가격, python3
from collections import deque

# testcase는 전부 통과하지만 효율성에서 실패하는 코드
# def solution(prices: list) -> list:
#     stack, second = [], 0  # stack: 결과값을 담을 list, second: 가격이 떨어지지 않은 기간을 담을 변수
#
#     for index, price in enumerate(prices):  # prices 배열 요소 for문 반복
#         if second != 0:  # secode가 0이 아닌경우 -> 즉, 아래 조건에서 현재 값과 다음 값들을 비교했을 때, 나머지 값들이 현재값보다 다 클 경우
#             stack.append(second)
#             second = 0
#         if index + 1 == len(prices):  # 마지막 요소일 시, stack에 0넣고 반복문 종료
#             stack.append(0)
#             break
#         for data in prices[index+1:]:  # 현재 반복문 요소와 다음 반복문들 비교하기 위해 for문 순회
#             if prices[index] <= data:  # 현재 요소보다 다음 요소들의 가격이 더 크거나 같을 시,
#                 second += 1            # +1 초
#             else:                      # 주식 가격이 떨어졌을 시,
#                 stack.append(second+1)  # stack에 값 추가 후 초 clear + break
#                 second = 0
#                 break
#
#     return stack

# queue를 활용해 testcase + 효율성까지 성공한 코드
def solution(prices: list) -> list:
    # result: 결과 값을 담을 변수, queue: prices list를 deque로 변환한 자료구조, second: 가격이 떨어지지 않은 기간을 담을 변수
    result, queue, second = [], deque(prices), 0

    while queue:  # queue에 값이 있을때까지 무한반복
        if second != 0:  # secode가 0이 아닌경우 -> 즉, 아래 조건에서 현재 값과 다음 값들을 비교했을 때, 나머지 값들이 현재값보다 다 클 경우
            result.append(second)
            second = 0
        if len(queue) == 1:  # 마지막 요소일 시, stack에 0넣고 반복문 종료
            result.append(0)
            break

        price = queue.popleft()  # 현재 반복문 요소 주식 가격 가져옴

        for data in queue:     # 현재 반복문 요소와 다음 반복문들 비교하기 위해 for문 순회
            if price <= data:  # 현재 주식가격보다 다음 요소들의 가격이 더 크거나 같을 시,
                second += 1    # + 1초
            else:              # 주식 가격이 떨어졌을 시,
                result.append(second+1)  # result list에 값 추가 후, 초 변수 clear + break
                second = 0
                break

    return result

if __name__ == '__main__':
    print(solution([1, 2, 3, 2, 3]))      # [4, 3, 1, 1, 0]
    print(solution([1, 2, 3, 2, 3, 1]))   # [5, 4, 1, 2, 1, 0]
    print(solution([5, 8, 6, 2, 4, 1]))   # [3, 1, 1, 2, 1, 0]