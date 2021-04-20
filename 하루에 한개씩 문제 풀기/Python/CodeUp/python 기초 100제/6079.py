import sys

num = int(sys.stdin.readline())
result = 0

for i in range(num+1):
    if result >= num:
        print(i-1)
        break
    result += i