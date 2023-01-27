# https://www.acmicpc.net/problem/2631
# boj, 2631: 줄 세우기, python3
import sys

input = sys.stdin.readline

def solve(n: int, nums: list) -> int:
    # dp table 초기화
    dp = [0] * (n+1)
    dp[0] = 1

    # dp bottom-up
    for x in range(1, n):
        l = [dp[y] for y in range(x) if nums[x] > nums[y]]
        if not l:
            dp[x] = 1
        else:
            dp[x] = max(l) + 1

    return n - max(dp)

if __name__ == '__main__':
    # 첫째 줄에는 아이들의 수 N이 주어진다.
    n = int(input())
    # 둘째 줄부터는 1부터 N까지의 숫자가 한 줄에 하나씩 주어진다.
    nums = [int(input()) for _ in range(n)]
    # 첫째 줄에는 번호 순서대로 줄을 세우는데 옮겨지는 아이들의 최소 수를 출력한다.
    print(solve(n, nums))