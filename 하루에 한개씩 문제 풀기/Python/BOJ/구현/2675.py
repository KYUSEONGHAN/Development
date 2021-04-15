# boj, 2675 : 문자열 반복, python3
import sys

T = int(sys.stdin.readline())

for i in range(T):
    R, S = map(str, sys.stdin.readline().split())
    R = int(R)

    for j in range(len(S)):
        print(S[j] * R, end='')
    print()