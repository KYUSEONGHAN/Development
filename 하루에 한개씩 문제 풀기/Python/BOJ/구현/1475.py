# boj, 1475 : 방 번호, python
import sys
import math


def Room_number(N):
    dasom = [0] * 9

    for n in N:
        if any((n == 6, n == 9)):
            dasom[5] += 0.5
        else:
            dasom[n] += 1

    answer = math.ceil(max(dasom))

    return answer


N = list(map(int, str(input())))

print(Room_number(N))