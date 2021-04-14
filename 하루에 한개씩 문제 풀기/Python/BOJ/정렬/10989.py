# 수정 전 메모리 초과 코드
# boj, 10989 : 수 정렬하기3, python3
import sys


def quick_sort(ARRAY):
    ARRAY_LENGTH = len(ARRAY)
    if (ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [element for element in ARRAY[1:] if element > PIVOT]
        LESSER = [element for element in ARRAY[1:] if element <= PIVOT]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)


N = int(input())
nums = [int(input()) for i in range(N)]

print(("\n").join(map(str, quick_sort(nums))))


# 수정 후 성공 코드
import sys

N = int(sys.stdin.readline())
nums = []
result = [0 for _ in range(10001)]

for i in range(N):
    num = int(sys.stdin.readline())
    result[num] += 1

for i in range(len(result)):
    for j in range(result[i]):
        print(i)