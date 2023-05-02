from typing import List

def get_max_value(n: int, m: int, a_list: List[int], b_list: List[int]) -> int:
    result = 0

    for i in range(0, n - m + 1):
        result = max(result, sum([x * y for x, y in zip(a_list[i:i + m], b_list)]))

    return result

def solve(n: int, m: int, a_list: List[int], b_list: List[int]) -> int:
    return get_max_value(n, m, a_list, b_list) if n >= m else get_max_value(m, n, a_list, b_list)

if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        n, m = map(int, input().split())
        a_list = list(map(int, input().split()))
        b_list = list(map(int, input().split()))

        print(f'#{test_case} {solve(n, m, a_list, b_list)}')