def cut_tongnamu(n: int) -> str:
    return 'Alice' if n%2 == 0 else 'Bob'

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    print(f'#{test_case} {cut_tongnamu(n)}')