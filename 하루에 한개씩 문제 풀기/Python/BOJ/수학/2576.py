# https://www.acmicpc.net/problem/2576
# boj, 2576: 홀수, python3
import sys

input = sys.stdin.readline

def solve(nums: list):
    hole_nums = [x for x in nums if x % 2 == 1]

    if hole_nums:
        print(sum(hole_nums))
        print(min(hole_nums))
    else:
        print(-1)

if __name__ == '__main__':
    nums = [int(input()) for _ in range(7)]

    solve(nums)