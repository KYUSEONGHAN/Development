def no_sleep(num: int) -> int:
    dict = {str(x): -1 for x in range(0, 9+1)}
    cnt, tmp = 1, num

    while True:
        for x in str(num):
            if x in dict:
                dict[x] += 1
        if -1 not in dict.values():
            break
        cnt += 1
        num = tmp * cnt

    return num


T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    print(f'#{test_case} {no_sleep(num)}')