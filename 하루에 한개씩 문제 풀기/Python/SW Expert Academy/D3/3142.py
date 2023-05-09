def solve(n: int, m: int) -> str:
    y = n - m
    x = m - y
    return ' '.join(map(str, (x, y)))

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    print(f'#{test_case} {solve(n, m)}')