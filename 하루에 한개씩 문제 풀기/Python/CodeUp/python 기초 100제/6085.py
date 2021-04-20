import sys

w, h, b = map(int,sys.stdin.readline().split())

print("%.2f MB" %(w*h*b/8/1024/1024))