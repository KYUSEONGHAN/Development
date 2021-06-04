# boj, 9375 : 패션왕 신해빈, python3
# 정수론 및 조합론
import sys


def fashion_king(n):
    if n == 0:
        return 0

    wearable = {}

    for _ in range(n):
        wear_name, wear_type = map(str, input().split())

        if wear_type in wearable.keys():
            wearable[wear_type] += 1
        else:
            wearable[wear_type] = 1

        answer = 1

        for key in wearable.keys():
            answer *= wearable[key] + 1

    return answer - 1


T = int(sys.stdin.readine())

for _ in range(T):
    n = int(sys.stdin.readline())
    print(fashion_king(n))