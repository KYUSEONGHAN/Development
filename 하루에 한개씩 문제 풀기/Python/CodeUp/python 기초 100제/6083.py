import sys

r, g, b = map(int, sys.stdin.readline().split())
cnt = 0

for i in range(r):
    for j in range(g):
        for n in range(b):
            print(i, j, n)
            cnt += 1

print(cnt)