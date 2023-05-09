def solve(s: str) -> str:
    score = sum([1 for x in s if x == 'o'])

    return 'YES' if 15 - len(s) + score >= 8 else 'NO'

T = int(input())

for test_case in range(1, T + 1):
    s = str(input())
    print(f'#{test_case} {solve(s)}')