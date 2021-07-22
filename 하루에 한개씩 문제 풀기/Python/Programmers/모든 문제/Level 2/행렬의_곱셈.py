# programmers, phase2:행렬의 곱셈, python3
# 본인 코드
import numpy as np


def solution(arr1, arr2):
    arr1, arr2 = np.array(arr1), np.array(arr2)

    return np.dot(arr1, arr2).tolist()


# 최적 코드
# - , - , - , 이도형 , Ezechiel_Kim 외 1 명
def solution(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]