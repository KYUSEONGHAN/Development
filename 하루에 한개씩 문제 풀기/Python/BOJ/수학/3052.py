# boj, 3052 : 나머지, python3
import sys

nums = [int(sys.stdin.readline()) for _ in range(10)]
nums_nameoji = [i%42 for i in nums]
result = list(set(nums_nameoji))

print(len(result))