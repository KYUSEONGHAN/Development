import sys

var = int(sys.stdin.readline(), 16)

for i in range(1,16):
    print('%X'%var, '*%X'%i, '=%X'%(var*i), sep='')