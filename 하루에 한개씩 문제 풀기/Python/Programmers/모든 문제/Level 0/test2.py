# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# kakao moblilty task 2, python
def solution(N: int, A: list, B: list) -> bool:
    list_range = []

    # 주어진 범의 중에 수가 하나라도 없으면 모든 정점을 거칠 수 없으므로 false를 반환
    for x in range(1, N+1):
        if x not in A + B:
            return False

    # for 반복문으로 순차적으로 두 list의 요소들 순회
    for index in range(len(A)):
        # 절댓값의 차가 1이면 하나씩 오름차순으로 통과할 수 있는 경로
        if abs(A[index] - B[index]) == 1:
            # 오름차순으로 통과하는 경로를 list에 append
            list_range.append([min(A[index], B[index]), max(A[index], B[index])])

    # 2차원 list 중복 제거
    re_range = set(map(tuple, list_range))

    # 모든 정점을 하나씩 오름차순으로 통과하는 경로이면 중복 제거한 list의 길이가 n-1과 같아야한다.
    return True if len(re_range) == N-1 else False


if __name__ == '__main__':
    print(solution(4, [1, 2, 4, 4, 3], [2, 3, 1, 3, 1]))  # true
    print(solution(4, [1, 2, 1, 3], [2, 4, 3, 4]))  # false
    print(solution(6, [2, 4, 5, 3], [3, 5, 6, 4]))  # false
    print(solution(3, [1, 3], [2, 2]))  # true

# n 정점, m 간선 -> 무방향 그래프
# 주어진 그래프에 정점 1부터 정점 n까지 모든 정점을 하나씩 오름차순으로 통과하는 경로가 있는지 확인