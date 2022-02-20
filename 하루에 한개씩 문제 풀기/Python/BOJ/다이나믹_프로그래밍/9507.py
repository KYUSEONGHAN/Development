# https://www.acmicpc.net/problem/9507
# boj, 9507: Generations of Tribbles, python3
import sys

input = sys.stdin.readline

def dp(n):
    # 앞서 계산된 결과를 저장하기 위한 dp 테이블 초기화
    d = [0] * 68
    # 문제 조건에서 정의된대로 값 할당
    d[0] = 1
    d[1] = 1
    d[2] = 2
    d[3] = 4

    # dp bottom-up
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3] + d[i-4]

    return d[n]

if __name__ == '__main__':
    t = int(input())
    nums = [int(input()) for _ in range(t)]

    for x in nums:
        print(dp(x))