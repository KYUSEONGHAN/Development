# https://www.acmicpc.net/problem/10807
# boj, 10807: 개수 세기, python3
import sys

input = sys.stdin.readline  # 변수 입력 속도 향상

# 입력으로 주어진 n개의 정수 중에 v가 몇 개인지 반환하느 함수
def solve(nums: list, v: int) -> int:
    return sum([1 for x in nums if x == v])

if __name__ == '__main__':
    n = int(input())  # 정수의 개수
    nums = list(map(int, input().split()))  # 정수가 공백으로 주어진다.
    v = int(input())  # 찾으려고 하는 정수 v

    print(solve(nums, v))