def solve(hour1: int, minute1: int, hour2: int, minute2: int) -> str:
    if minute1 + minute2 >= 60:
        minute = minute1 + minute2 - 60
        hour1 += 1
    else:
        minute = minute1 + minute2

    if hour1 + hour2 > 12:
        hour = hour1 + hour2 - 12
    else:
        hour = hour1 + hour2

    return ' '.join(map(str, [hour, minute]))


T = int(input())

for test_case in range(1, T + 1):
    hour1, minute1, hour2, minute2 = map(int, input().split())

    print(f'#{test_case} {solve(hour1, minute1, hour2, minute2)}')