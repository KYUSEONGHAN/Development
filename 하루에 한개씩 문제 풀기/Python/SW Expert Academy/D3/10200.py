def gudok_war(n: int, a: int, b: int) -> str:
    max_value = min(a, b)
    min_value = a + b - n if a + b >= n else 0
    return ' '.join(map(str, [max_value, min_value]))

T = int(input())

for test_case in range(1, T + 1):
    n, a, b = map(int, input().split())
    print(f'#{test_case} {gudok_war(n, a, b)}')
