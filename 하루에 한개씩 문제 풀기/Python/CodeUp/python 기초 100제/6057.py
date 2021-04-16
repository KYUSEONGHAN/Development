import sys

num1, num2 = map(int,sys.stdin.readline().split())
num1 = bool(num1)
num2 = bool(num2)

if num1 is num2:
    print('True')
else:
    print('False')