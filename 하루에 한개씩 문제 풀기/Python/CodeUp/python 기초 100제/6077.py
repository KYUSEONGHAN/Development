import sys

num = int(sys.stdin.readline())

result = [i for i in range(num+1) if i%2 ==0]

print(sum(result))