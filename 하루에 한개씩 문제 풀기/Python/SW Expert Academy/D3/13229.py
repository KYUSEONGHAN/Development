def sunday(day: str) -> int:
    dict = {"MON": 6, "TUE": 5, "WED": 4, "THU": 3, "FRI": 2, "SAT": 1, "SUN": 7}
    return dict[day]

T = int(input())

for test_case in range(1, T + 1):
    day = str(input())
    print(f'#{test_case} {sunday(day)}')