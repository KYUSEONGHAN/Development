# https://www.acmicpc.net/problem/2460
# boj, 2460: 지능형 기차 2, python3
def solve(nums: list) -> int:
    result, max_num = [], 0

    for x in nums:
        out_num, in_num = x
        max_num += in_num - out_num
        result.append(max_num)

    return max(result)

if __name__ == '__main__':
    nums = [list(map(int, input().split())) for _ in range(10)]

    print(solve(nums))