# boj, 2108 : 통계학, python3
import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

nums.sort()

top_num = Counter(nums).most_common()

print("%.f" % (sum(nums) / N))
print(nums[N // 2])

if len(nums) > 1:
    if top_num[0][1] == top_num[1][1]:
        print(top_num[1][0])
    else:
        print(top_num[0][0])
else:
    print(nums[0])

print(nums[-1] - nums[0])