# boj, 1000 : A + B, python3
import sys

A, B = map(int,sys.stdin.readline().split())

if A > 10 or A < 0:
    print("A range error")
elif B > 10 or B < 0:
    print("B range error")
else:
    print(A+B)