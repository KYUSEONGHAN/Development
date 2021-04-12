# boj, 11022 : a + b - 8 , python3
import sys

T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int,input().split())
    print("Case #%d: %d + %d = %d"%(i+1,A,B,A+B))