def solve(data: str) -> int:
    result = 0

    for x in range(len(data) - 1):
        if data[x:x + 2] == '(|' or data[x:x + 2] == '|)' or data[x:x + 2] == '()':
            result += 1

    return result


T = int(input())

for test_case in range(1, T + 1):
    s = str(input())
    print(f'#{test_case} {solve(s)}')