# boj, 2447 : 별 찍기 -10, python3
import sys


def star_shooting(N):
    star = [['*' for _ in range(N)] for _ in range(N)]
    cnt = 0
    divide = N

    while divide != 1:
        divide /= 3
        cnt += 1

    for n in range(cnt):
        idx = [i for i in range(N) if (i // 3 ** n) % 3 == 1]

        for i in idx:
            for j in idx:
                star[i][j] = " "

    for _ in star:
        print("".join(_))


N = int(sys.stdin.readline())

star_shooting(N)
