# https://www.acmicpc.net/problem/2592
# boj, 2592: 대푯값, python3
import sys

input = sys.stdin.readline

def solve(nums: list):
    # 입력받은 수들이 몇 번 선언되었는지 구하기위해 dict 초기화
    dict = {}
    result1 = sum(nums) // 10

    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1

    print(result1)                  # 평균
    print(max(dict, key=dict.get))  # 최빈값


if __name__ == '__main__':
    nums = [int(input()) for _ in range(10)]

    solve(nums)