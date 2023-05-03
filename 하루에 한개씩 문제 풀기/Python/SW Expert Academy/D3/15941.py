def parallelogram(n: int) -> int:
    return n * n

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    print(f'#{test_case} {parallelogram(n)}')