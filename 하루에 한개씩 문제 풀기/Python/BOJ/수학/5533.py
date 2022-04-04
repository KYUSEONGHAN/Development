# https://www.acmicpc.net/problem/5533
# boj, 5533: 유니크, python3
import sys

input = sys.stdin.readline

def solve(nums: list) -> str:
    trans, filter_l, result = [], [], []

    for x in range(3):
        l = []
        for y in nums:
            l.append(y[x])
        trans.append(l)

    for x in trans:
        l = []
        for y in x:
            if x.count(y) == 1:
                l.append(y)
            else:
                l.append(0)
        filter_l.append(l)

    result = list(zip(filter_l[0], filter_l[1], filter_l[2]))

    return '\n'.join(map(str, [sum(x) for x in result]))

if __name__ == '__main__':
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]

    print(solve(nums))