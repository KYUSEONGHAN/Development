def halfhalf(s: str) -> str:
    dict = {}

    for x in s:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1

    if len(dict.keys()) == 2:
        for _, value in dict.items():
            if value != 2:
                return 'No'
    else:
        return 'No'
    return 'Yes'


T = int(input())

for test_case in range(1, T + 1):
    s = str(input())
    print(f'#{test_case} {halfhalf(s)}')
