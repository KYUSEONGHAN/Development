def solve(idx: int, nums: list):
    return '#' + str(idx), sum([x for x in nums if x % 2 == 1])

if __name__ == '__main__':
    t = int(input())

    for idx in range(1, t+1):
        nums = list(map(int, input().split()))
        print(*solve(idx, nums))