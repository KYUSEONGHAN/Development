# boj, 1783 : 병든 나이트, python3
import sys

N, M = map(int,sys.stdin.readline().split())

if N is 1:
    print(1)
elif N is 2:
    print(min(4, (M + 1)//2))
elif N >= 3:
    if M <= 6:
        print(min(M, 4))
    else:
        print(M - 2)