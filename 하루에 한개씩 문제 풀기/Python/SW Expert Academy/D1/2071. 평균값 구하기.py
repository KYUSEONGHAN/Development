def solve(cnt: int, nums: list) -> str:
    return "#" + str(cnt) + " " + str(round(sum(nums) / len(nums)))

if __name__ == '__main__':
    n = int(input())

    for cnt in range(1, n+1):
        nums = list(map(int, input().split()))

        print(solve(cnt, nums))