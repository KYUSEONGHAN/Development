import sys

n = int(sys.stdin.readline())
k = list(map(int,sys.stdin.readline().split()))

k.reverse()

print(" ".join(map(str,k)))