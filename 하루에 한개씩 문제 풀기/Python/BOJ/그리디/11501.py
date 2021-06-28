# boj, 11501 : 주식, python
import sys


def share(n, l):
    result = 0
    target = l[0]

    for i in range(1, n):
        if l[i] > target:
            target = l[i]
        else:
            result += target - l[i]

    return result


for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    l = list((map(int, sys.stdin.readline().split())))
    print(share(N, list(reversed(l))))