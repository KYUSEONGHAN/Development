def check_num_type(num: int) -> str:
    return 'Odd' if num%2 == 1 else 'Even'

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    print(f'#{test_case} {check_num_type(num)}')