def zigzag_num(num: int) -> int:
    return sum([x if x%2 == 1 else -x for x in range(1, num+1)])

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    print(f'#{test_case} {zigzag_num(num)}')