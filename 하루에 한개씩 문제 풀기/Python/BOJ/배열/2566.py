# https://www.acmicpc.net/problem/2566
# boj, 2566: 최댓값, python3
def solve(nums: list):
    max_num, result = -1, []

    for x in range(9):
        for y in range(9):
            if max_num < nums[x][y]:
                max_num = nums[x][y]
                result.append([max_num, x+1, y+1])

    max_num, x, y = result[-1]

    print(max_num)
    print(x, y)

if __name__ == '__main__':
    nums = [list(map(int, input().split())) for _ in range(9)]

    solve(nums)