# boj, 1267: 핸드폰 요금, python3
import sys

input = sys.stdin.readline

def solve(times: list) -> str:
    minshik, yeongho = 0, 0

    for x in range(2):
        for time in times:
            if x == 0:
                minshik += (time // 30 + 1) * 10
            else:
                yeongho += (time // 60 + 1) * 15

    if minshik == yeongho:
        return f'Y M {minshik}'
    elif minshik > yeongho:
        return f'M {yeongho}'
    else:
        return f'Y {minshik}'

if __name__ == '__main__':
    n = int(input())
    times = list(map(int, input().split()))

    print(solve(times))