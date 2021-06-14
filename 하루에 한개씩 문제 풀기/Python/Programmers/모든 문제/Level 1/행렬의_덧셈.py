# programmers, phase1 : 행렬의 덧셈, python
def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        arr_sum = []
        for j in range(len(arr1[0])):
            arr_sum.append(arr1[i][j] + arr2[i][j])
        answer.append(arr_sum)

    return answer


# 최적코드
# - , 탈퇴한 사용자 , - , - , - 외 12 명 코드 참고
def sumMatrix(A, B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] += B[i][j]
    return A
