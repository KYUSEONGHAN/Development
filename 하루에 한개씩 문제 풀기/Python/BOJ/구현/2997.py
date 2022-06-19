# https://www.acmicpc.net/problem/2997
# boj, 2997: 네 번째 수, python3
import sys

input = sys.stdin.readline

# 까먹은 수를 반환하는 함수
def solve(nums: list) -> int:
    nums.sort()  # 상근이가 고른 수 오름차순 정렬
    diff = nums[1] - nums[0]

    if nums[2] - nums[1] == diff:
        return nums[-1] + diff
    elif nums[2] - nums[1] > diff:
        return nums[1] + diff
    elif nums[2] - nums[1] < diff:
        return nums[-1] - diff
if __name__ == '__main__':
    nums = list(map(int, input().split()))  # 상근이가 고른 4개의 수 중 3개

    print(solve(nums))