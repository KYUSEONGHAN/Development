import sys

nums = list(map(int,sys.stdin.readline().split()))
result = [i for i in nums if i%2 == 0]

print("\n".join(map(str,result)))