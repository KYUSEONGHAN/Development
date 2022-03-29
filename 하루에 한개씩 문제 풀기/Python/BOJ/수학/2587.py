# https://www.acmicpc.net/problem/2587
# boj, 2587: 대푯값2, python3
import sys

input = sys.stdin.readline

def solve(nums: list) -> str:
    result = []

    result.append(sum(nums)//5)  # avg
    result.append(nums[2])       # center

    return '\n'.join(map(str, result))

if __name__ == '__main__':
    nums = sorted([int(input()) for _ in range(5)])

    print(solve(nums))