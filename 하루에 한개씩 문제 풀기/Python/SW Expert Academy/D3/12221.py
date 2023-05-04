def gugudan2(a: int, b: int) -> int:
    return a * b if a <= 9 and b <= 9 else -1

T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int,input().split())
    print(f'#{test_case} {gugudan2(a, b)}')