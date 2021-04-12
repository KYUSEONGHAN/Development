# boj, 10430 : 나머지, python3
import sys

A, B, C = map(int,sys.stdin.readline().split())

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)