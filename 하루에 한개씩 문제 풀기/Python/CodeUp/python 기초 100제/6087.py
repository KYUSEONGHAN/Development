import sys

num = int(sys.stdin.readline())
result = [i for i in range(1,num+1) if i%3 != 0]

print(" ".join(map(str,result)))