def hour(a: int, b: int) -> int:
    return a + b - 24 if a + b >= 24 else a + b

T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'#{test_case} {hour(a, b)}')