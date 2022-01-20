# boj, 1292: 쉽게 푸는 문제, python3
import sys

input = sys.stdin.readline

def solve(a, b):
    num = []

    for x in range(1, b+1):
        for y in range(x):
            num.append(x)

    return sum(num[:b]) - sum(num[:a-1])

if __name__ == '__main__':
    a, b = map(int, input().split())

    print(solve(a, b))