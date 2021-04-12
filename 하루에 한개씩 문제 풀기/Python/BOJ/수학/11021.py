# boj, 11021 : a + b - 7, python3
import sys

T = int(sys.stdin.readline())

for i in range(1,T+1):
    A, B = map(int,sys.stdin.readline().split())
    print("Case #{}: {}".format(i,A+B))