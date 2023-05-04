def group_homework(n: int) -> int:
    return 0 if n <= 2 else n // 3

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    print(f'#{test_case} {group_homework(n)}')