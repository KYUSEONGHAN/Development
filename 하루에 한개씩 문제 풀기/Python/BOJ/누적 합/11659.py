# https://www.acmicpc.net/problem/11659
# boj, 11659: 구간 합 구하기 4, python3
import sys

input = sys.stdin.readline

# 주어진 구간의 누적 합을 반환하는 함수
def solve(d: list, start: int, end: int) -> int:
    # return sum(nums[start-1:end])  # 시간 초과
    return d[end - 1] - d[start - 1] + nums[start - 1]

if __name__ == '__main__':
    n, m = map(int, input().split())  # n: 수의 개수, m: 합을 구해야 하는 횟수
    nums = list(map(int, input().split()))  # nums: 주어진 수 list

    d = [0] * n  # dp table 초기화
    d[0] = nums[0]

    for x in range(1, n):  # dp bottom-up
        d[x] = d[x - 1] + nums[x]

    for _ in range(m):
        i, j = map(int, input().split())  # i:합을 구해야 하는 구간 시발점 j: 합을 구해야하는 구간 종결점

        print(solve(d, i, j))