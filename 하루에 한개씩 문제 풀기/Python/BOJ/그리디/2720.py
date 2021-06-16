# boj, 2720 : 세탁소 사장 동혁, python3
# 그리디 알고리즘
import sys


def donghyuk(money):
    result = [0, 0, 0, 0]  # $0.25, $0.10, $0.05, $0.01
    coin = [25, 10, 5, 1]

    for i in range(len(coin)):
        result[i] += money // coin[i]
        money %= coin[i]

    return ' '.join(map(str, result))


T = int(input())

for _ in range(T):
    C = int(sys.stdin.readline())
    print(donghyuk(C))