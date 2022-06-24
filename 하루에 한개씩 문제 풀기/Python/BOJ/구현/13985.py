# https://www.acmicpc.net/problem/13985
# boj, 13985: equality, python3

# 주어진 식이 옳바른지 아닌지 판별하는 함수
def solve(express: list) -> str:
    return 'YES' if int(express[0]) + int(express[2]) == int(express[-1]) else 'NO'

if __name__ == '__main__':
    express = input().split()

    print(solve(express))