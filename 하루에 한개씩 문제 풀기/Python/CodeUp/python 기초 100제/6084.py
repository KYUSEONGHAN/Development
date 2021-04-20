import sys

h, b, c, s = map(int,sys.stdin.readline().split())

print("%.1f MB" %(h*b*c*s/1024/1024/8))