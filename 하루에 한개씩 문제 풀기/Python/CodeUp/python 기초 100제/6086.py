import sys

num = int(sys.stdin.readline())
result = 0

if num == 1:
    print(1)
else:
    for i in range(1,num+1):
        if result >= num:
            print(result)
            break
        result += i