def get_length(*args) -> int:
    dict = {}

    for x in args:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1

    for key, value in dict.items():
        if value != 2:
            return key


T = int(input())

for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())
    print(f'#{test_case} {get_length(a, b, c)}')