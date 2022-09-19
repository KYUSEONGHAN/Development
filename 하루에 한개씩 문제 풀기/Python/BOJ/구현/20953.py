# https://www.acmicpc.net/problem/20953
# boj, 20953: 고고학자 예린, python3
import sys

input = sys.stdin.readline

# def dolmen(a: int, b: int) -> int:
#     sum, k = 0, 0
#
#     for _ in range(0, a + b):
#         for j in range(0, a + b):
#             while k < j:
#                 sum += 1
#                 k += 1
#             k = 0
#
#     return sum
def dolmen(a: int, b: int) -> int:
    return (a + b) * (a + b - 1) * (a + b) // 2


if __name__ == '__main__':
    t = int(input())  # 테스트 케이스의 개수

    for _ in range(t):
        a, b = map(int, input().split())

        print(dolmen(a, b))