import sys

num = int(sys.stdin.readline())
result = ['X' if i%10 == 3 or i%10 ==6 or i%10 ==9 else i for i in range(1,num+1)]

print(" ".join(map(str,result)))