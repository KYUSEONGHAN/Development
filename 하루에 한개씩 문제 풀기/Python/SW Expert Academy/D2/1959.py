from typing import List


def solve(n: int, m: int, a_list: List[int], b_list: List[int]) -> int:
    result = 0

    if n >= m:
        for i in range(0, n-m+1):
            nums = a_list[i:i+m]
            result = max(result, sum([x*y for x, y in zip(nums, b_list)]))
    else:
        for i in range(0, m-n+1):
            nums = b_list[i:i+n]
            result = max(result, sum([x*y for x, y in zip(nums, a_list)]))

    return result

if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        n, m = map(int, input().split())
        a_list = list(map(int, input().split()))
        b_list = list(map(int, input().split()))

        print(f'#{test_case} {solve(n, m, a_list, b_list)}')