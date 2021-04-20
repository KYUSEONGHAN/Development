import sys

a, m, d, n = map(int,sys.stdin.readline().split())

for i in range(n - 1):
    a = a * m + d

print(a)