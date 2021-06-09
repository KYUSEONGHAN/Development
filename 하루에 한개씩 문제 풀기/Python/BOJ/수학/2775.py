# boj, 2775 : 부녀회장이 될테야, python3
# 수학 알고리즘
import sys


def solve(num1, num2):
    floor_0 = [i for i in range(1, num2 + 1)]

    for _ in range(num1):
        for j in range(1, num2):
            floor_0[j] += floor_0[j - 1]

    return floor_0[-1]


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        k = int(sys.stdin.readline())
        n = int(sys.stdin.readline())
        print(solve(k, n))